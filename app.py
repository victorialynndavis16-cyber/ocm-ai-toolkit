from html import escape

import streamlit as st

from questions import EODI_DIMENSIONS, SCALE_LABELS
from skills import (
    assess_value_conversion_risk,
    calculate_average_maturity_score,
    calculate_dimension_scores,
    calculate_structural_integrity_score,
    diagnose_constraint_stack,
    draft_executive_summary,
    normalize_scores,
    prepare_workshop_agenda,
    recommend_actions,
)


def format_scale_help(helper_text: str | None = None) -> str:
    """Create slider help text from the editable labels in questions.py."""
    scale_help = f"1 = {SCALE_LABELS[1]}, 5 = {SCALE_LABELS[5]}"

    if helper_text:
        return f"{helper_text} {scale_help}."

    return scale_help


def build_constraint_stack_chart(
    normalized_scores: dict[str, float],
    dimension_scores: dict[str, float],
) -> str:
    """Build a ranked, accessible horizontal bar chart for the diagnostic readout."""
    ranked_scores = sorted(normalized_scores.items(), key=lambda item: item[1])
    chart_rows = []

    for rank, (dimension, normalized_score) in enumerate(ranked_scores, start=1):
        role = "Primary Constraint" if rank == 1 else f"Rank {rank}"
        dimension_label = escape(dimension)
        score_label = (
            f"{role}: {normalized_score:.2f} normalized "
            f"({dimension_scores[dimension]:.1f} / 5 average)"
        )
        bar_color = "#334155" if rank == 1 else "#64748b"
        width_percent = round(normalized_score * 100, 1)

        chart_rows.append(
            f"""
            <div class="constraint-row">
                <div class="constraint-meta">
                    <span class="constraint-rank">{rank}. {dimension_label}</span>
                    <span class="constraint-score">{escape(score_label)}</span>
                </div>
                <div class="constraint-track" aria-hidden="true">
                    <div
                        class="constraint-bar"
                        style="width: {width_percent}%; background: {bar_color};"
                    ></div>
                </div>
            </div>
            """
        )

    accessible_summary = "; ".join(
        f"{rank}. {dimension}, {normalized_score:.2f} normalized"
        for rank, (dimension, normalized_score) in enumerate(ranked_scores, start=1)
    )

    return f"""
    <style>
        .constraint-stack-chart {{
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 1rem;
            background: #ffffff;
        }}
        .constraint-chart-title {{
            color: #0f172a;
            font-size: 1rem;
            font-weight: 700;
            margin-bottom: 0.75rem;
        }}
        .constraint-row {{
            margin-bottom: 0.85rem;
        }}
        .constraint-row:last-child {{
            margin-bottom: 0;
        }}
        .constraint-meta {{
            align-items: baseline;
            display: flex;
            gap: 0.75rem;
            justify-content: space-between;
            margin-bottom: 0.25rem;
        }}
        .constraint-rank {{
            color: #0f172a;
            font-size: 0.95rem;
            font-weight: 650;
        }}
        .constraint-score {{
            color: #475569;
            font-size: 0.88rem;
            text-align: right;
        }}
        .constraint-track {{
            background: #e2e8f0;
            border-radius: 999px;
            height: 0.7rem;
            overflow: hidden;
            width: 100%;
        }}
        .constraint-bar {{
            border-radius: 999px;
            height: 100%;
            min-width: 0.2rem;
        }}
        @media (max-width: 700px) {{
            .constraint-meta {{
                align-items: flex-start;
                flex-direction: column;
                gap: 0.1rem;
            }}
            .constraint-score {{
                text-align: left;
            }}
        }}
    </style>
    <section
        class="constraint-stack-chart"
        role="img"
        aria-label="Constraint Stack by EODI Dimension. {escape(accessible_summary)}"
    >
        <div class="constraint-chart-title">Constraint Stack by EODI Dimension</div>
        {''.join(chart_rows)}
    </section>
    """



def main() -> None:
    # Page settings control the browser title, page icon, and layout.
    st.set_page_config(
        page_title="EODI Diagnostic Prototype",
        page_icon=":bar_chart:",
        layout="wide",
    )

    st.title("Executive Operating Discipline Index")
    st.write(
        "EODI measures whether an executive team has the operating discipline "
        "required to convert AI capability into enterprise value."
    )
    st.info(
        "This is a constraint-based diagnostic: the structural score uses the "
        "geometric mean so the weakest operating-model elements constrain the result."
    )

    with st.form("eodi_diagnostic_form"):
        st.subheader("Diagnostic context")

        organization_name = st.text_input(
            "Organization or executive team",
            placeholder="Example: Enterprise Operations Leadership Team",
        )
        ai_context = st.text_input(
            "AI agenda or use case focus",
            placeholder="Example: AI-enabled service operations transformation",
        )

        st.subheader("Diagnostic questions")
        st.caption(
            "Use 1 for weak operating discipline and 5 for strong operating discipline. "
            "For friction questions, the app reverses the score during calculation."
        )

        responses = {}

        for dimension, questions in EODI_DIMENSIONS.items():
            st.markdown(f"### {dimension}")
            responses[dimension] = []

            for index, question_config in enumerate(questions):
                question = question_config["question"]
                responses[dimension].append(
                    st.slider(
                        question,
                        min_value=1,
                        max_value=5,
                        value=3,
                        help=format_scale_help(question_config.get("helper_text")),
                        key=f"{dimension}_{index}",
                    )
                )

        submitted = st.form_submit_button("Run EODI diagnostic")

    if not submitted:
        st.caption("Complete the diagnostic form to generate EODI outputs.")
        return

    context = {
        "organization_name": organization_name,
        "ai_context": ai_context,
    }

    # Calculate dimension averages, normalize to 0-1, and compare structural
    # integrity against a simple maturity average.
    dimension_scores = calculate_dimension_scores(responses)
    normalized_scores = normalize_scores(dimension_scores)
    structural_integrity_score = calculate_structural_integrity_score(normalized_scores)
    average_maturity_score = calculate_average_maturity_score(normalized_scores)
    constraint_stack = diagnose_constraint_stack(normalized_scores)
    top_constraint = constraint_stack[0]
    value_conversion_risk = assess_value_conversion_risk(structural_integrity_score)
    recommended_actions = recommend_actions(constraint_stack)
    executive_summary = draft_executive_summary(
        context,
        structural_integrity_score,
        average_maturity_score,
        constraint_stack,
        value_conversion_risk,
    )
    workshop_agenda = prepare_workshop_agenda(constraint_stack)

    st.subheader("Diagnostic outputs")

    metric_columns = st.columns(4)
    metric_columns[0].metric(
        "EODI Structural Integrity Score",
        f"{structural_integrity_score:.2f}",
    )
    metric_columns[1].metric(
        "Average Maturity Score",
        f"{average_maturity_score:.2f}",
    )
    metric_columns[2].metric("Top Constraint", top_constraint)
    metric_columns[3].metric("Value Conversion Risk", value_conversion_risk)

    st.subheader("Dimension scores")
    for dimension, score in normalized_scores.items():
        raw_average = dimension_scores[dimension]
        st.progress(
            score,
            text=f"{dimension}: {score:.2f} normalized ({raw_average:.1f} / 5 average)",
        )

    st.subheader("Constraint Stack")
    st.caption(
        "Ranked from lowest EODI score to highest. The first bar is labeled "
        "Primary Constraint because it is the strongest limiter in the current readout."
    )
    st.markdown(
        build_constraint_stack_chart(normalized_scores, dimension_scores),
        unsafe_allow_html=True,
    )

    st.subheader("Executive summary")
    st.markdown(executive_summary)

    st.subheader("Recommended actions")
    for constraint, actions in recommended_actions.items():
        st.markdown(f"**{constraint}**")
        for action in actions:
            st.checkbox(action, value=False, key=f"{constraint}_{action}")

    st.subheader("90-minute workshop agenda")
    for agenda_item in workshop_agenda:
        st.write(
            f"**{agenda_item['time']} - {agenda_item['topic']}**: "
            f"{agenda_item['purpose']}"
        )


if __name__ == "__main__":
    main()
