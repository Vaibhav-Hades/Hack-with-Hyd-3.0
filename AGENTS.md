# AGENTS.md

## Purpose
`AGENTS.md` is the single source of truth for **all AI coding assistants** working on the RESOLVE project. Every assistant must read this file (and the referenced documentation) before performing any action.

## Repository locations
- Project root: `d:/Hack with Hyd 3.0`
- Documentation folder: `Docs/`

## Core documents (must be consulted)
| Aspect | Document | When to read |
|--------|----------|--------------|
| Project vision & scope | `Docs/PROJECT.md` | Any task – provides purpose, target users, non‑goals. |
| System architecture | `Docs/ARCHITECTURE.md` | Backend or frontend work that touches component boundaries. |
| API contract | `Docs/API_CONTRACT.md` | All integration work – frontend, backend, tests. |
| Memory model | `Docs/MEMORY_ARCHITECTURE.md` | Any AI/agent or Hindsight‑related implementation. |
| Data model | `Docs/DATA_MODEL.md` | Database schema changes, migrations. |
| UI spec | `Docs/UI_SPECIFICATION.md` | Frontend component design. |
| Development workflow | `Docs/DEVELOPMENT_RULES.md` | Every code change – outlines AI workflow and human rules. |
| Integration workflow | `Docs/INTEGRATION_RULES.md` | Coordinating frontend/backend changes. |
| Demo flow | `Docs/DEMO_FLOW.md` | When creating example data or demo scripts. |
| Change log | `CHANGELOG.md` | Review past decisions before altering architecture. |

## Ownership boundaries (must not be crossed)
- **Frontend** (`/Frontend`): UI pages, components, TypeScript types, API client.  Respect the contract; never call Hindsight directly.
- **Backend** (`/Backend`): FastAPI server, business logic, AI agent orchestration, Hindsight & LLM integration.  Do not modify UI files.
- **Database** (`/DB`): SQL schema, migration scripts, seed data.  No UI or API code here.
- **Memory**: Hindsight is accessed **only** from the backend AI agent layer.
- **Structured state**: PostgreSQL is accessed via the backend repository layer only.

## Safety & verification rules
1. **Read‑only first** – always `view_file` any file you intend to edit.
2. **Plan** – respond with a concise plan before performing edits.
3. **Edit tooling** – use `replace_file_content` for a single contiguous change, `multi_replace_file_content` for multiple non‑adjacent edits.
4. **Testing** – after any code change run the appropriate lint/test command and report the results.
5. **No secrets** – never write real credentials; use placeholders from `.env.example`.
6. **AI Task Completion Protocol** – always end your response with the mandated sections (Completed, Files Changed, Verification, Integration Impact, Known Issues, Recommended Next Task, Copy‑Paste Next Prompt).

## Parallel development protocol
- Follow `Docs/INTEGRATION_RULES.md` for PR workflow and contract updates.
- When you modify an API contract, add a comment in the contract file explaining *why* and then **notify** the other developer (e.g., via a PR comment).
- Update TypeScript types and mock data **immediately** after any backend contract change.

## Required steps for any AI‑initiated change
1. **Read `AGENTS.md`** (this file).
2. **Read the specific project docs** related to the task.
3. **Inspect the target files** with `view_file`.
4. **Explain your plan** in the response.
5. **Implement** using the appropriate edit tool.
6. **Run validation** (lint/tests) and capture output.
7. **Report** using the completion protocol.
8. **Suggest the next concrete task** and provide a ready‑to‑paste prompt.

---
*Last updated: 2026‑09‑28*
