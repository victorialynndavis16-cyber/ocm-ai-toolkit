# EODI Diagnostic Prototype

The Executive Operating Discipline Index (EODI) is a Streamlit prototype for
assessing whether an executive team has the operating discipline required to
convert AI capability into enterprise value.

The core thesis is constraint-based: AI value is limited by the weakest elements
of the operating model. A company can have strong AI tools, but if decision
velocity, incentives, talent mobility, capital reallocation, or executive fluency
are weak, AI productivity will not reliably convert into economic outcomes.

## Dimensions

The app scores five EODI dimensions:

- Decision Velocity
- Incentive Alignment
- Talent Redeployment
- Capital Reallocation
- Executive Fluency

Each dimension includes four diagnostic questions scored on a 1-5 slider. The
app averages each dimension, normalizes the result to 0-1, and calculates:

- EODI Structural Integrity Score using the geometric mean
- Average Maturity Score using a simple average
- Constraint Stack showing the lowest three dimensions
- Top Constraint
- Value Conversion Risk
- Executive summary
- Recommended actions
- 90-minute workshop agenda

## How the Files Work Together

- `app.py` contains the Streamlit user interface. It collects context, captures
  question-level slider responses, and displays diagnostic outputs.
- `questions.py` contains the editable EODI dimension names, question wording,
  helper text, scale labels, and reverse-scoring flags. Start here when changing
  question wording or labels.
- `skills.py` contains deterministic scoring, constraint diagnosis,
  recommendations, executive summary, and workshop agenda logic.
- `prompts.py` stores reusable text instructions for a future AI-enabled version
  of the prototype. The current app does not call an external AI API.
- `AGENTS.md` gives Codex repo-level guidance for keeping the prototype simple,
  readable, deterministic, and executive-ready.
- `requirements.txt` lists the Python package needed to run the Streamlit app.

## Run in Replit

1. Create a new Replit Python project.
2. Upload or import this repository.
3. Confirm `requirements.txt` includes:

```text
streamlit>=1.33,<2
```

4. In the Replit shell, install dependencies:

```bash
pip install -r requirements.txt
```

5. Run the app:

```bash
streamlit run app.py --server.address=0.0.0.0 --server.port=3000
```

6. Open the Replit web preview.

## Current Limitations

- The prototype uses deterministic scoring logic only.
- It does not call external APIs.
- Scores are directional and should be paired with stakeholder discussion.
- Recommended actions and agendas are generated from fixed templates.
- Friction-oriented questions are reverse-scored so higher final scores always
  indicate stronger operating discipline.
