# This file contains the deterministic "skills" for the OCM Diagnostic Agent.
# There are no external AI calls yet. Each function uses simple Python logic so
# new learners can read, edit, and extend the prototype.


# OCM-oriented recommendations for each diagnostic dimension.
# The app selects recommendations based on the lowest-scoring constraints.
INTERVENTION_LIBRARY = {
    "Leadership Alignment": [
        "Facilitate an executive alignment session to confirm the case for change, sponsor roles, and success measures.",
        "Create a visible sponsor action plan with specific leadership messages, decisions, and engagement moments.",
        "Translate the AI use case into business outcomes leaders can consistently reinforce.",
    ],
    "Decision Velocity": [
        "Clarify decision rights for funding, process changes, data access, risk review, and go-live approval.",
        "Create a weekly decision forum to remove blockers and keep the AI initiative moving.",
        "Document a lightweight pilot governance path so teams know how decisions will be made.",
    ],
    "Workforce Capability": [
        "Segment impacted audiences by role and define the skills each group needs to adopt the AI-enabled workflow.",
        "Build practical enablement materials such as role guides, manager talking points, and hands-on demos.",
        "Create office hours or peer support channels so employees can ask questions as the change lands.",
    ],
    "Governance Maturity": [
        "Use a responsible AI checklist before pilots move into production or broad adoption.",
        "Assign review owners for privacy, security, legal, compliance, operational risk, and model quality.",
        "Define how AI outputs will be monitored, escalated, and improved after launch.",
    ],
    "Reinforcement Mechanisms": [
        "Add adoption progress, risks, and wins to existing leadership routines and team meetings.",
        "Define behavior-based adoption measures so teams know what good use looks like.",
        "Recognize teams that demonstrate safe, useful, and repeatable AI-enabled ways of working.",
    ],
}


def assess_readiness(dimension_scores: dict[str, int]) -> float:
    """Calculate the overall readiness score across the five dimensions."""
    # The overall score is the average of the dimension scores.
    total_score = sum(dimension_scores.values())
    number_of_dimensions = len(dimension_scores)

    return total_score / number_of_dimensions


def diagnose_constraints(
    dimension_scores: dict[str, int],
    number_of_constraints: int = 3,
) -> list[str]:
    """Return the lowest-scoring dimensions as the top OCM constraints."""
    # Sort dimensions from lowest score to highest score.
    # If two dimensions have the same score, Python keeps the original order.
    sorted_dimensions = sorted(dimension_scores, key=dimension_scores.get)

    # Return only the number of constraints requested by the caller.
    return sorted_dimensions[:number_of_constraints]


def recommend_interventions(top_constraints: list[str]) -> dict[str, list[str]]:
    """Generate practical OCM interventions for each top constraint."""
    interventions = {}

    for constraint in top_constraints:
        interventions[constraint] = INTERVENTION_LIBRARY[constraint]

    return interventions


def draft_executive_summary(
    context: dict[str, str],
    overall_score: float,
    dimension_scores: dict[str, int],
    top_constraints: list[str],
) -> str:
    """Draft a short executive-ready summary of the diagnostic results."""
    # Pull context values out of the dictionary. If a field is blank, use a
    # simple fallback phrase so the summary still reads cleanly.
    organization_name = context.get("organization_name") or "the organization"
    change_initiative = context.get("change_initiative") or "the change initiative"
    impacted_audience = context.get("impacted_audience") or "the impacted audience"
    ai_use_case = context.get("ai_use_case") or "the AI use case"

    strongest_dimension = max(dimension_scores, key=dimension_scores.get)
    primary_constraint = top_constraints[0]

    if overall_score >= 4:
        readiness_level = "strong"
    elif overall_score >= 3:
        readiness_level = "moderate"
    else:
        readiness_level = "early-stage"

    return (
        f"**{organization_name}** shows **{readiness_level} readiness** for "
        f"**{change_initiative}** with an overall score of **{overall_score:.1f} out of 5**. "
        f"The diagnostic indicates that **{strongest_dimension}** is currently the strongest "
        f"OCM condition, while **{primary_constraint}** is the most important constraint to "
        f"address for **{impacted_audience}**. For the AI use case, **{ai_use_case}**, leaders "
        "should focus first on the recommended interventions tied to the top constraints before "
        "expanding adoption."
    )


def prepare_workshop_agenda(top_constraints: list[str]) -> list[dict[str, str]]:
    """Create a 90-minute workshop agenda focused on the top constraints."""
    # The agenda is intentionally simple and deterministic. It gives change
    # leaders a practical meeting structure they can reuse immediately.
    primary_constraint = top_constraints[0]
    secondary_constraint = top_constraints[1] if len(top_constraints) > 1 else "the next constraint"
    tertiary_constraint = top_constraints[2] if len(top_constraints) > 2 else "sustainment risks"

    return [
        {
            "time": "0-10 min",
            "topic": "Set context and outcomes",
            "purpose": "Confirm the AI use case, impacted audience, and decisions needed from the session.",
        },
        {
            "time": "10-25 min",
            "topic": "Review readiness diagnostic",
            "purpose": "Discuss the overall score, dimension scores, and what they imply for adoption risk.",
        },
        {
            "time": "25-45 min",
            "topic": f"Deep dive on {primary_constraint}",
            "purpose": "Identify root causes, owner gaps, and immediate actions for the top constraint.",
        },
        {
            "time": "45-60 min",
            "topic": f"Plan interventions for {secondary_constraint}",
            "purpose": "Select practical OCM interventions and clarify who must be involved.",
        },
        {
            "time": "60-75 min",
            "topic": f"Address {tertiary_constraint}",
            "purpose": "Confirm supporting actions needed to reduce adoption friction and sustain behavior change.",
        },
        {
            "time": "75-90 min",
            "topic": "Confirm owners, next steps, and leadership messages",
            "purpose": "Assign owners, agree on timing, and define the executive message coming out of the workshop.",
        },
    ]
