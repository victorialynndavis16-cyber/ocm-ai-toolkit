import streamlit as st


DIMENSIONS = {
    "Strategy": "Clear goals, sponsorship, and a prioritized AI use-case portfolio.",
    "Data": "Accessible, governed, and trusted data for AI-enabled workflows.",
    "People": "Skills, role clarity, and change readiness across impacted teams.",
    "Process": "Repeatable ways to test, launch, monitor, and improve AI solutions.",
    "Risk": "Responsible AI controls for privacy, security, compliance, and quality.",
}

RECOMMENDATIONS = {
    "Strategy": "Define two or three high-value use cases, name an executive sponsor, and agree on success metrics before scaling.",
    "Data": "Inventory the data needed for priority use cases and close gaps in ownership, quality, and access.",
    "People": "Create a role-based enablement plan so leaders, managers, and frontline teams know how AI changes their work.",
    "Process": "Stand up a lightweight pilot process with intake, experiment reviews, launch criteria, and feedback loops.",
    "Risk": "Document responsible AI guardrails and assign review owners for privacy, security, legal, and operational risks.",
}

ACTION_PLANS = {
    "Strategy": [
        "Confirm the business outcomes AI should support in the next 90 days.",
        "Select one executive sponsor and one operational owner for each priority use case.",
        "Create a value scorecard covering impact, feasibility, adoption risk, and measurement.",
    ],
    "Data": [
        "Map the data sources required for each priority use case.",
        "Assign data owners and define minimum quality checks before pilots begin.",
        "Document access, privacy, and retention requirements for sensitive data.",
    ],
    "People": [
        "Identify the roles most affected by the AI-enabled workflow.",
        "Build targeted enablement for leaders, managers, practitioners, and support teams.",
        "Create a feedback channel for employee concerns, training needs, and adoption blockers.",
    ],
    "Process": [
        "Define a pilot intake and approval workflow.",
        "Set launch criteria for accuracy, usability, adoption readiness, and support coverage.",
        "Schedule post-launch reviews to measure value and capture improvements.",
    ],
    "Risk": [
        "Create a responsible AI checklist for privacy, security, compliance, and human oversight.",
        "Name reviewers for high-risk use cases before testing begins.",
        "Define escalation steps for inaccurate, biased, unsafe, or unexpected AI outputs.",
    ],
}


def readiness_band(score: float) -> tuple[str, str]:
    if score >= 4:
        return "Ready to scale", "Your foundations are strong. Focus on governance, measurement, and repeatable adoption."
    if score >= 3:
        return "Ready for focused pilots", "You have a workable base. Pick narrow pilots and close the biggest readiness gaps."
    if score >= 2:
        return "Needs preparation", "Build the basics before launching broad AI initiatives."
    return "Early stage", "Start with alignment, education, and a small number of low-risk discovery activities."


def executive_summary(scores: dict[str, int], band: str, lowest_dimension: str) -> str:
    strongest_dimension = max(scores, key=scores.get)
    return (
        f"The organization is currently **{band.lower()}**. "
        f"The strongest readiness area is **{strongest_dimension}**, while **{lowest_dimension}** "
        "is the most important gap to address before expanding AI adoption."
    )


def main() -> None:
    st.set_page_config(page_title="AI Adoption Readiness", page_icon="OCM", layout="wide")

    st.title("AI Adoption Readiness App")
    st.write("Assess organizational readiness across strategy, data, people, process, and risk.")

    scores = {}
    with st.form("readiness_assessment"):
        st.subheader("Readiness score")
        for dimension, description in DIMENSIONS.items():
            scores[dimension] = st.slider(
                dimension,
                min_value=1,
                max_value=5,
                value=3,
                help=description,
            )

        notes = st.text_area(
            "Context notes",
            placeholder="Add business unit, audience, target use cases, or adoption concerns.",
        )
        submitted = st.form_submit_button("Calculate readiness")

    if submitted:
        average_score = sum(scores.values()) / len(scores)
        band, guidance = readiness_band(average_score)
        lowest_dimension = min(scores, key=scores.get)

        metric_cols = st.columns(3)
        metric_cols[0].metric("Overall score", f"{average_score:.1f} / 5")
        metric_cols[1].metric("Readiness band", band)
        metric_cols[2].metric("Priority gap", lowest_dimension)

        st.subheader("Guidance")
        st.markdown(executive_summary(scores, band, lowest_dimension))
        st.write(guidance)
        st.info(RECOMMENDATIONS[lowest_dimension])

        st.subheader("Recommended actions")
        for action in ACTION_PLANS[lowest_dimension]:
            st.checkbox(action, value=False)

        st.subheader("Dimension detail")
        for dimension, score in scores.items():
            st.progress(score / 5, text=f"{dimension}: {score}/5")

        if notes.strip():
            st.subheader("Notes")
            st.write(notes)
    else:
        st.caption("Use the sliders and calculate readiness to see recommendations.")


if __name__ == "__main__":
    main()
