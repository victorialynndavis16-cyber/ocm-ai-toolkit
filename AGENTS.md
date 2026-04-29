# Codex Instructions

This repository is an Executive Operating Discipline Index (EODI) diagnostic
prototype. The app helps executive teams assess whether their operating model
can convert AI capability into enterprise value.

## Development Guidance

- Keep the code simple, readable, and beginner-friendly.
- Use Streamlit only unless the user explicitly asks for another framework.
- Avoid unnecessary dependencies.
- Preserve consulting-quality language for executives.
- Prefer clear comments and readable functions over clever abstractions.
- Keep deterministic logic in `skills.py` unless an external AI workflow is
  explicitly requested later.
- Keep `app.py` focused on the Streamlit user interface.
- Treat EODI as a constraint-based diagnostic, not a generic readiness score.
- When behavior changes, update `README.md` so the documentation stays current.
