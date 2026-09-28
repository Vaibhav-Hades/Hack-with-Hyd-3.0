# DEVELOPMENT_RULES.md

## General Principles
- **Inspect before edit**: Always view existing files (especially Docs and code) before making any changes.
- **Minimal impact**: Modify only the files directly related to the task. Never touch unrelated modules.
- **Scope awareness**: Respect the ownership boundaries defined in `ARCHITECTURE.md`.
- **No speculative features**: Do not add functionality that is not explicitly requested in the project roadmap.
- **Stay provider‑agnostic**: Do not hard‑code a specific LLM or cloud service unless the spec demands it.

## Code Modification Rules
1. **Read‑only**: Files not under your responsibility must remain untouched.
2. **Single‑purpose edits**: Use the appropriate edit tool (`replace_file_content` for a single contiguous change, `multi_replace_file_content` for multiple non‑adjacent changes).
3. **Preserve documentation**: Keep existing comments and docstrings unless a change is required for clarity.
4. **No secret leakage**: Never commit real API keys, passwords, or tokens. Use placeholders in `.env.example`.
5. **Testing & Validation**:
   - Run `npm run lint` (frontend) or `pytest`/`flake8` (backend) after changes.
   - Ensure all unit tests pass before committing.
6. **Commit hygiene**:
   - One logical change per commit.
   - Write concise, descriptive commit messages.
   - Reference the related documentation file in the commit body.

## Dependency Management
- **Avoid bloat**: Add new dependencies only after a clear justification and after discussing with the team lead.
- **Lock versions**: Use exact version pins in `requirements.txt` or `package.json`.

## Review Process
- Submit a **pull request** with a clear description of the change.
- Ensure the PR references the relevant documentation sections.
- Request review from the other developer; incorporate feedback before merging.

## AI Assistant Workflow (Required for all AI agents)
1. **Read `AGENTS.md`** – primary instruction set.
2. **Read any related Docs** (e.g., `PROJECT.md`, `ARCHITECTURE.md`).
3. **Inspect affected files** via `view_file`.
4. **Plan** – write a brief plan in the response before editing.
5. **Implement** – use the appropriate edit tool.
6. **Verify** – run lint/tests, report results.
7. **Report** – follow the **AI Task Completion Protocol** (section 18 of the spec).
8. **Suggest next step** with a ready‑to‑paste prompt.

---
*Last updated: 2026‑09‑28*
