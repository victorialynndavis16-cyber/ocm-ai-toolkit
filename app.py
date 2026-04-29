import streamlit as st

from skills import (
    assess_readiness,
    diagnose_constraints,
    draft_executive_summary,
    prepare_workshop_agenda,
    recommend_interventions,
)


# These are the five OCM diagnostic dimensions used by the prototype.
# The Streamlit interface asks the user to score each dimension from 1 to 5.
DIMENSIONS = [
    "Leadership Alignment",
    "Decision Velocity",
    "Workforce Capability",
    "Governance Maturity",
    "Reinforcement Mechanisms",
]


def main() -> None:
    # Streamlit page settings control the browser title, page icon, and layout.
    st.set_page_config(
        page_title="OCM Diagnostic Agent",
        page_icon="OCM",
        layout="wide",
    )

    st.title("OCM Diagnostic Agent")
    st.write(
        "Assess AI adoption readiness, diagnose the top organizational constraints, "
        "and generate practical OCM interventions."
    )

    # The form collects the business context and readiness scores in one place.
    # The diagnostic skills run only after the user submits the form.
    with st.form("ocm_diagnostic_form"):
        st.subheader("Diagnostic context")

        organization_name = st.text_input(
            "Organization or team name",
            placeholder="Example: Enterprise Operations Team",
        )
        change_initiative = st.text_input(
            "Change initiative",
            placeholder="Example: AI-enabled service request triage",
        )
        impacted_audience = st.text_input(
            "Impacted audience",
            placeholder="Example: Service desk analysts and team leads",
        )
        ai_use_case = st.text_area(
            "AI use case",
            placeholder="Example: Use AI to summarize intake requests and recommend routing.",
        )

        st.subheader("Readiness scores")
        st.caption("Use 1 for low readiness and 5 for high readiness.")

        dimension_scores = {}
        for dimension in DIMENSIONS:
            dimension_scores[dimension] = st.slider(
                dimension,
                min_value=1,
                max_value=5,
                value=3,
                help="1 = low readiness, 5 = high readiness",
            )

        submitted = st.form_submit_button("Run OCM diagnostic")

    if submitted:
        # Store the context in a dictionary so it can be passed cleanly to skills.
        context = {
            "organization_name": organization_name,
            "change_initiative": change_initiative,
            "impacted_audience": impacted_audience,
            "ai_use_case": ai_use_case,
        }

        # Run the five deterministic OCM Diagnostic Agent skills.
        overall_score = assess_readiness(dimension_scores)
        top_constraints = diagnose_constraints(dimension_scores)
        interventions = recommend_interventions(top_constraints)
        executive_summary = draft_executive_summary(
            context,
            overall_score,
            dimension_scores,
            top_constraints,
        )
        workshop_agenda = prepare_workshop_agenda(top_constraints)

        st.subheader("Diagnostic outputs")

        metric_columns = st.columns(2)
        metric_columns[0].metric("Overall readiness score", f"{overall_score:.1f} / 5")
        metric_columns[1].metric("Top constraint", top_constraints[0])

        st.subheader("Dimension scores")
        for dimension, score in dimension_scores.items():
            st.progress(score / 5, text=f"{dimension}: {score} / 5")

        st.subheader("Top constraints")
        for constraint in top_constraints:
            st.write(f"- {constraint}")

        st.subheader("Recommended interventions")
        for constraint, actions in interventions.items():
            st.markdown(f"**{constraint}**")
            for action in actions:
                st.checkbox(action, value=False, key=f"{constraint}_{action}")

        st.subheader("Executive summary")
        st.markdown(executive_summary)

        st.subheader("90-minute workshop agenda")
        for agenda_item in workshop_agenda:
            st.write(
                f"**{agenda_item['time']} - {agenda_item['topic']}**: "
                f"{agenda_item['purpose']}"
            )
    else:
        st.caption("Complete the diagnostic form to generate OCM recommendations.")


if __name__ == "__main__":
    main()
