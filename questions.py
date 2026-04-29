# Edit this file when you want to update the diagnostic question wording.
#
# Suggested workflow:
# 1. Make wording or formatting changes in questions.py.
# 2. Run the app in Replit.
# 3. Test the flow as a user.
# 4. If output logic feels wrong, update skills.py.
# 5. If screen layout feels wrong, update app.py.
# 6. Commit the finished change to GitHub.
#
# For most wording edits, update only:
# - dimension names
# - question text
# - helper_text
# - SCALE_LABELS
#
# Leave reverse_score unchanged unless you are intentionally changing the
# scoring model. Reverse-scored questions describe friction, so their raw
# 1-5 slider value is flipped during scoring.


SCALE_LABELS = {
    1: "Weak operating discipline",
    2: "Developing operating discipline",
    3: "Mixed or inconsistent operating discipline",
    4: "Strong operating discipline",
    5: "Very strong operating discipline",
}


EODI_DIMENSIONS = {
    "Decision Velocity": [
        {
            "question": "How quickly are AI-related decisions made once a use case is identified?",
            "helper_text": "Consider the time between identifying a use case and making the decisions needed to move forward.",
            "reverse_score": False,
        },
        {
            "question": "How often are decisions revisited or reversed after initial agreement?",
            "helper_text": "Frequent reversals indicate friction, so this question is reverse-scored.",
            "reverse_score": True,
        },
        {
            "question": "How clearly are decision rights defined for AI initiatives?",
            "helper_text": "Consider whether teams know who approves, escalates, funds, and accepts risk.",
            "reverse_score": False,
        },
        {
            "question": "How frequently do AI initiatives stall due to unclear ownership or escalation?",
            "helper_text": "Frequent stalls indicate friction, so this question is reverse-scored.",
            "reverse_score": True,
        },
    ],
    "Incentive Alignment": [
        {
            "question": "Are leaders measured on outcomes enabled by AI (not just activity)?",
            "helper_text": "Consider whether leadership measures value created, not only pilots launched or tools deployed.",
            "reverse_score": False,
        },
        {
            "question": "Do current incentives encourage adoption of new workflows?",
            "helper_text": "Consider whether people are rewarded for changing how work gets done.",
            "reverse_score": False,
        },
        {
            "question": "How often do employees revert to old ways of working despite new tools?",
            "helper_text": "Frequent reversion indicates friction, so this question is reverse-scored.",
            "reverse_score": True,
        },
        {
            "question": "Are productivity gains captured and tied to performance expectations?",
            "helper_text": "Consider whether efficiency gains are visible, expected, and managed.",
            "reverse_score": False,
        },
    ],
    "Talent Redeployment": [
        {
            "question": "When AI creates efficiency, is capacity actively reallocated?",
            "helper_text": "Consider whether freed capacity is deliberately moved to higher-value work.",
            "reverse_score": False,
        },
        {
            "question": "How quickly can teams shift people to higher-value work?",
            "helper_text": "Consider how easily managers can change responsibilities, priorities, and staffing.",
            "reverse_score": False,
        },
        {
            "question": "Are there clear processes for redeploying talent?",
            "helper_text": "Consider whether leaders have a repeatable process once AI removes work from a role or workflow.",
            "reverse_score": False,
        },
        {
            "question": "How often does freed capacity go unused?",
            "helper_text": "Unused capacity indicates friction, so this question is reverse-scored.",
            "reverse_score": True,
        },
    ],
    "Capital Reallocation": [
        {
            "question": "How quickly is budget reallocated based on AI-driven insights?",
            "helper_text": "Consider whether funding can move when evidence shows a better use of capital.",
            "reverse_score": False,
        },
        {
            "question": "Are savings from AI initiatives reinvested into higher-value opportunities?",
            "helper_text": "Consider whether savings are intentionally redirected rather than absorbed invisibly.",
            "reverse_score": False,
        },
        {
            "question": "How flexible are funding mechanisms for new AI initiatives?",
            "helper_text": "Consider whether promising initiatives can get resources without waiting for a long budget cycle.",
            "reverse_score": False,
        },
        {
            "question": "How often do promising initiatives stall due to funding constraints?",
            "helper_text": "Frequent funding stalls indicate friction, so this question is reverse-scored.",
            "reverse_score": True,
        },
    ],
    "Executive Fluency": [
        {
            "question": "How frequently do executives engage directly with AI tools?",
            "helper_text": "Consider whether leaders have hands-on exposure to AI in real workflows.",
            "reverse_score": False,
        },
        {
            "question": "How comfortable are leaders in evaluating AI-driven decisions?",
            "helper_text": "Consider whether leaders can challenge AI outputs, assumptions, risks, and business implications.",
            "reverse_score": False,
        },
        {
            "question": "Are AI risks and governance actively discussed at leadership levels?",
            "helper_text": "Consider whether governance is part of executive operating conversations.",
            "reverse_score": False,
        },
        {
            "question": "How often are AI capabilities incorporated into strategic planning?",
            "helper_text": "Consider whether AI capability changes planning assumptions, choices, and priorities.",
            "reverse_score": False,
        },
    ],
}
