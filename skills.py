# These recommendations are used by the agent when it finds the lowest-scoring
# dimension, also called the top constraint.
RECOMMENDED_ACTIONS = {
    "Leadership Alignment": [
        "Hold a leadership alignment session to define the AI adoption vision.",
        "Name an executive sponsor and decision owner for each priority AI use case.",
        "Create a simple scorecard that connects AI work to business outcomes.",
    ],
    "Decision Velocity": [
        "Map the approval process for AI pilots and remove unnecessary handoffs.",
        "Set decision rights for budget, data access, risk review, and launch approval.",
        "Create a weekly blocker review for active AI experiments.",
    ],
    "Workforce Capability": [
        "Build role-based training for leaders, managers, and impacted employees.",
        "Create manager talking points for explaining AI-enabled workflow changes.",
        "Set up office hours or coaching support for teams using new AI tools.",
    ],
    "Governance Maturity": [
        "Create a responsible AI checklist for each pilot before launch.",
        "Define review owners for privacy, security, legal, compliance, and quality.",
        "Monitor AI outputs and user feedback after release.",
    ],
    "Reinforcement Mechanisms": [
        "Add AI adoption progress to existing leadership and team routines.",
        "Collect employee feedback at 30, 60, and 90 days after launch.",
        "Recognize teams that demonstrate safe, useful, and repeatable AI adoption.",
    ],
}


# Agent Skill 1:
# Calculate the overall readiness score across every question in the assessment.
def calculate_overall_readiness_score(all_scores: dict[str, list[int]]) -> float:
    every_score = []

    for question_scores in all_scores.values():
        every_score.extend(question_scores)

    return sum(every_score) / len(every_score)


# Agent Skill 2:
# Calculate one average score for each readiness dimension.
def calculate_dimension_scores(all_scores: dict[str, list[int]]) -> dict[str, float]:
    dimension_scores = {}

    for dimension, question_scores in all_scores.items():
        dimension_scores[dimension] = sum(question_scores) / len(question_scores)

    return dimension_scores


# Agent Skill 3:
# Find the lowest-scoring dimension. This is the top constraint because it is
# the area most likely to limit AI adoption progress.
def identify_top_constraint(dimension_scores: dict[str, float]) -> str:
    return min(dimension_scores, key=dimension_scores.get)


# Agent Skill 4:
# Return recommended actions based on the top constraint.
def generate_recommended_actions(top_constraint: str) -> list[str]:
    return RECOMMENDED_ACTIONS[top_constraint]


# Agent Skill 5:
# Create a short executive summary that a leader can quickly scan.
def generate_executive_summary(
    overall_score: float,
    dimension_scores: dict[str, float],
    top_constraint: str,
) -> str:
    strongest_dimension = max(dimension_scores, key=dimension_scores.get)

    if overall_score >= 4:
        readiness_level = "strong"
    elif overall_score >= 3:
        readiness_level = "moderate"
    else:
        readiness_level = "early"

    return (
        f"The organization shows **{readiness_level} AI adoption readiness** "
        f"with an overall score of **{overall_score:.1f} out of 5**. "
        f"The strongest area is **{strongest_dimension}**, while the top constraint is "
        f"**{top_constraint}**. Focus first on this constraint to improve adoption momentum."
    )
