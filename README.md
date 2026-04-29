# OCM Diagnostic Agent

The OCM Diagnostic Agent is a Streamlit prototype for assessing AI adoption
readiness and turning the results into practical change-management guidance.

Use it to capture a quick readiness baseline and identify the next best adoption actions.

## How it works
Users respond to questions across key dimensions:
- Leadership alignment
- Decision-making clarity
- Workforce capability
- Governance maturity
- Reinforcement mechanisms
It collects context about an organization, change initiative, impacted audience,
and AI use case, then scores five OCM readiness dimensions:

- Leadership Alignment
- Decision Velocity
- Workforce Capability
- Governance Maturity
- Reinforcement Mechanisms

The app produces an overall readiness score, dimension scores, top constraints,
recommended interventions, an executive summary, and a 90-minute workshop agenda.

## How the Files Work Together

- `app.py` contains the Streamlit user interface. It collects inputs and displays
  diagnostic outputs.
- `skills.py` contains deterministic diagnostic functions for readiness scoring,
  constraint diagnosis, recommendations, executive summaries, and workshop agendas.
- `prompts.py` stores reusable text instructions for a future AI-enabled version
  of the agent. The current app does not call an external AI API.
- `AGENTS.md` gives Codex repo-level guidance for keeping the prototype simple,
  readable, and OCM-oriented.
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
streamlit run app.py --server.address 0.0.0.0 --server.port 3000
```

6. Open the Replit web preview.

## Current Limitations

- The prototype uses deterministic scoring logic only.
- It does not call an external AI API.
- Recommendations are based on the lowest-scoring readiness dimensions.
- Workshop agendas are generated from a fixed structure.
- Scores are directional and should be paired with stakeholder discussion.

## Next Planned Enhancements

- Add richer question-level scoring under each dimension.
- Add downloadable diagnostic reports.
- Add configurable intervention libraries by industry or function.
- Add optional AI-generated summaries after guardrails are defined.
- Add session storage or export options for workshop facilitation.
