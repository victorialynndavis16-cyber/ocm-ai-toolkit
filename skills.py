# This file contains the deterministic skills for the EODI diagnostic prototype.
# There are no external AI calls. The calculations are intentionally simple so
# the model can be reviewed and adapted by business users and developers.

from math import prod

from questions import EODI_DIMENSIONS


RECOMMENDATION_LIBRARY = {
    "Decision Velocity": [
        "Define decision rights for AI use case approval, risk acceptance, funding, data access, and operating-model changes.",
        "Create a weekly executive decision forum for escalations that block AI value conversion.",
        "Set decision service levels so teams know when issues must be resolved or escalated.",
    ],
    "Incentive Alignment": [
        "Tie leadership scorecards to economic outcomes enabled by AI, not pilots launched or tools deployed.",
        "Update performance expectations so teams are rewarded for adopting improved workflows.",
        "Measure whether productivity gains are captured, redeployed, or lost back into legacy work patterns.",
    ],
    "Talent Redeployment": [
        "Create a capacity redeployment process triggered when AI removes work from a role or workflow.",
        "Maintain a prioritized backlog of higher-value work that can absorb freed capacity quickly.",
        "Assign owners to track whether AI-enabled efficiency becomes redeployed talent, better service, or lower cost.",
    ],
    "Capital Reallocation": [
        "Establish a lightweight funding mechanism for scaling AI use cases with demonstrated operating impact.",
        "Create rules for reinvesting AI-driven savings into higher-value growth, productivity, or risk-reduction opportunities.",
        "Review budget allocation monthly against evidence from AI-enabled workflows and performance data.",
    ],
    "Executive Fluency": [
        "Run hands-on executive AI working sessions using the company's actual workflows and decisions.",
        "Give leaders a shared rubric for evaluating AI outputs, risks, governance needs, and economic implications.",
        "Build AI capability review into strategic planning, operating reviews, and capital allocation discussions.",
    ],
}


def score_question(raw_score: int, reverse_score: bool) -> int:
    """Return a directionally consistent 1-5 score for one question."""
    if reverse_score:
        return 6 - raw_score

    return raw_score


def calculate_dimension_scores(responses: dict[str, list[int]]) -> dict[str, float]:
    """Average the four question scores within each EODI dimension."""
    dimension_scores = {}

    for dimension, questions in EODI_DIMENSIONS.items():
        adjusted_scores = []

        for index, question_config in enumerate(questions):
            raw_score = responses[dimension][index]
            adjusted_scores.append(
                score_question(raw_score, question_config["reverse_score"])
            )

        dimension_scores[dimension] = sum(adjusted_scores) / len(adjusted_scores)

    return dimension_scores


def normalize_scores(dimension_scores: dict[str, float]) -> dict[str, float]:
    """Convert 1-5 dimension scores to a 0-1 scale."""
    return {
        dimension: (score - 1) / 4
        for dimension, score in dimension_scores.items()
    }


def calculate_structural_integrity_score(normalized_scores: dict[str, float]) -> float:
    """Calculate EODI using the geometric mean of normalized dimensions."""
    # A small floor prevents one zero score from collapsing the entire prototype
    # to zero while still heavily penalizing the weakest operating constraint.
    floor = 0.01
    adjusted_scores = [max(score, floor) for score in normalized_scores.values()]

    return prod(adjusted_scores) ** (1 / len(adjusted_scores))


def calculate_average_maturity_score(normalized_scores: dict[str, float]) -> float:
    """Calculate the simple average score for comparison."""
    return sum(normalized_scores.values()) / len(normalized_scores)


def diagnose_constraint_stack(
    normalized_scores: dict[str, float],
    number_of_constraints: int = 3,
) -> list[str]:
    """Return the lowest-scoring dimensions as the constraint stack."""
    sorted_dimensions = sorted(normalized_scores, key=normalized_scores.get)

    return sorted_dimensions[:number_of_constraints]


def assess_value_conversion_risk(structural_integrity_score: float) -> str:
    """Translate the structural score into an executive risk level."""
    if structural_integrity_score >= 0.75:
        return "Low"
    if structural_integrity_score >= 0.55:
        return "Moderate"
    if structural_integrity_score >= 0.35:
        return "Elevated"

    return "High"


def recommend_actions(constraint_stack: list[str]) -> dict[str, list[str]]:
    """Select recommended actions for the lowest-scoring dimensions."""
    return {
        constraint: RECOMMENDATION_LIBRARY[constraint]
        for constraint in constraint_stack
    }


def draft_executive_summary(
    context: dict[str, str],
    structural_integrity_score: float,
    average_maturity_score: float,
    constraint_stack: list[str],
    value_conversion_risk: str,
) -> str:
    """Draft a concise executive summary of the EODI result."""
    organization_name = context.get("organization_name") or "the executive team"
    ai_context = context.get("ai_context") or "the current AI agenda"
    top_constraint = constraint_stack[0]

    return (
        f"**{organization_name}** has an EODI Structural Integrity Score of "
        f"**{structural_integrity_score:.2f}** and an Average Maturity Score of "
        f"**{average_maturity_score:.2f}** for **{ai_context}**. The gap between these "
        f"measures matters: the structural score reflects the EODI thesis that AI value "
        f"is constrained by the weakest elements of the operating model. The top "
        f"constraint is **{top_constraint}**, creating **{value_conversion_risk.lower()} "
        "value conversion risk** unless leadership addresses the constraint stack before "
        "scaling AI activity further."
    )


def prepare_workshop_agenda(constraint_stack: list[str]) -> list[dict[str, str]]:
    """Create a 90-minute workshop agenda focused on the constraint stack."""
    top_constraint = constraint_stack[0]
    second_constraint = constraint_stack[1]
    third_constraint = constraint_stack[2]

    return [
        {
            "time": "0-10 min",
            "topic": "Frame the value conversion problem",
            "purpose": "Confirm the AI value thesis, target outcomes, and why operating discipline is the gating factor.",
        },
        {
            "time": "10-25 min",
            "topic": "Review EODI results",
            "purpose": "Compare the structural integrity score, average maturity score, and dimension-level results.",
        },
        {
            "time": "25-45 min",
            "topic": f"Deep dive on {top_constraint}",
            "purpose": "Identify the root causes, leadership decisions, and operating-model changes required for the top constraint.",
        },
        {
            "time": "45-60 min",
            "topic": f"Pressure-test {second_constraint}",
            "purpose": "Clarify where the second constraint could block AI value conversion and what must change.",
        },
        {
            "time": "60-75 min",
            "topic": f"Address {third_constraint}",
            "purpose": "Select actions that reduce the third constraint and support the overall operating model.",
        },
        {
            "time": "75-90 min",
            "topic": "Commit to actions and owners",
            "purpose": "Assign owners, deadlines, and leadership routines for improving the constraint stack.",
        },
    ]
