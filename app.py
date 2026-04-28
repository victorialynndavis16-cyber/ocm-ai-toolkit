import streamlit as st

from skills import (
    calculate_dimension_scores,
    calculate_overall_readiness_score,
    generate_executive_summary,
    generate_recommended_actions,
    identify_top_constraint,
)


# This dictionary defines the five readiness dimensions for the prototype.
# Each dimension has three scored questions that will be shown as sliders.
DIMENSIONS = {
    "Leadership Alignment": [
        "Leaders share a clear vision for how AI will support business outcomes.",
        "Executive sponsors are actively involved in AI adoption decisions.",
        "AI priorities are connected to the organization's strategic goals.",
    ],
    "Decision Velocity": [
        "Teams can make timely decisions about AI opportunities and tradeoffs.",
        "AI pilots have clear approval paths and decision owners.",
        "Leaders can quickly remove blockers that slow AI adoption.",
    ],
    "Workforce Capability": [
        "Employees understand how AI may change their day-to-day work.",
        "Teams have access to practical AI training and support.",
        "Managers are prepared to coach teams through AI-enabled change.",
    ],
    "Governance Maturity": [
        "The organization has clear guidance for responsible AI use.",
        "Privacy, security, legal, and compliance risks are reviewed before launch.",
        "AI solutions are monitored for quality, accuracy, and unintended impacts.",
    ],
    "Reinforcement Mechanisms": [
        "AI adoption goals are reinforced through communication and leadership routines.",
        "Teams collect feedback after AI tools are introduced.",
        "Successful AI behaviors are recognized, measured, and sustained over time.",
    ],
}


def main() -> None:
    # Page setup controls the browser tab title, page icon, and layout width.
    st.set_page_config(
        page_title="AI Adoption Readiness Agent",
        page_icon="AI",
        layout="wide",
    )

    st.title("AI Adoption Readiness Agent")
    st.write(
        "Use this prototype to score AI adoption readiness, identify the top constraint, "
        "and generate practical next actions."
    )

    # This dictionary will store the user's slider scores for each dimension.
    assessment_scores = {}

    # A Streamlit form keeps the assessment tidy and only runs the analysis after
    # the user clicks the submit button.
    with st.form("ai_readiness_assessment"):
        st.subheader("Readiness assessment")

        for dimension, questions in DIMENSIONS.items():
            st.markdown(f"### {dimension}")
            assessment_scores[dimension] = []

            for question_number, question in enumerate(questions, start=1):
                score = st.slider(
                    label=question,
                    min_value=1,
                    max_value=5,
                    value=3,
                    help="1 = low readiness, 5 = high readiness",
                    key=f"{dimension}_{question_number}",
                )
                assessment_scores[dimension].append(score)

        submitted = st.form_submit_button("Run readiness agent")

    if submitted:
        # Run the five agent skills after the user submits the assessment.
        overall_score = calculate_overall_readiness_score(assessment_scores)
        dimension_scores = calculate_dimension_scores(assessment_scores)
        top_constraint = identify_top_constraint(dimension_scores)
        recommended_actions = generate_recommended_actions(top_constraint)
        summary = generate_executive_summary(
            overall_score,
            dimension_scores,
            top_constraint,
        )

        st.subheader("Agent results")

        metric_columns = st.columns(2)
        metric_columns[0].metric("Overall readiness score", f"{overall_score:.1f} / 5")
        metric_columns[1].metric("Top constraint", top_constraint)

        st.subheader("Executive summary")
        st.markdown(summary)

        st.subheader("Dimension-level scores")
        for dimension, score in dimension_scores.items():
            st.progress(score / 5, text=f"{dimension}: {score:.1f} / 5")

        st.subheader("Recommended actions")
        for action in recommended_actions:
            st.checkbox(action, value=False)
    else:
        st.caption("Complete the sliders and run the readiness agent to see results.")


if __name__ == "__main__":
    main()
