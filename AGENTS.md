# Codex Instructions

This repository is an OCM and AI adoption diagnostic prototype. The app helps
change leaders assess readiness, diagnose organizational constraints, recommend
OCM interventions, draft an executive summary, and prepare a workshop agenda.

## Development Guidance

- Keep the code simple, readable, and beginner-friendly.
- Use Streamlit only unless the user explicitly asks for another framework.
- Avoid unnecessary dependencies.
- Preserve consulting-quality language for executives and change leaders.
- Prefer clear comments and readable functions over clever abstractions.
- Keep deterministic logic in `skills.py` unless an external AI workflow is
  explicitly requested later.
- Keep `app.py` focused on the Streamlit user interface.
- When behavior changes, update `README.md` so the documentation stays current.
