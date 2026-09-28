# INTEGRATION_RULES.md

## Parallel Development Workflow

### Ownership
- **Developer 1** – Backend, AI agent, Hindsight integration, PostgreSQL schema, API implementation.
- **Developer 2** – Frontend (Next.js) UI, API client, TypeScript types, mock data.

### Contract‑First Development
1. **API contract first** – All backend endpoints must conform to `Docs/API_CONTRACT.md`.
2. **Mock‑first frontend** – Frontend developers implement UI against the static JSON examples in the contract until the backend delivers real responses.
3. **Change propagation** – If an endpoint must change:
   - Update the contract file.
   - Add a short rationale as a comment in the contract.
   - Notify the other developer (e.g., via a comment on the PR or a direct message).
   - Both sides must update their code (backend implementation / frontend types) before merging.

### Synchronisation Steps
| Step | Action | Owner |
|------|--------|-------|
| 1 | Create/modify an endpoint in `API_CONTRACT.md` | Backend |
| 2 | Open a PR on the backend with implementation stub (or placeholder) | Backend |
| 3 | Add or update TypeScript interfaces in `Frontend/src/types` reflecting the contract | Frontend |
| 4 | Write or adjust mock data files in `Frontend/mocks` matching the contract examples | Frontend |
| 5 | Run integration tests (e.g., using `jest` with `msw` or `pytest` with `httpx`) to ensure compatibility | Both |
| 6 | Merge when both sides have green checks and the contract is version‑consistent | Both |

### Versioning
- Minor, backward‑compatible changes (adding optional fields) can be made without bumping a major version, but must be documented in the contract.
- Breaking changes require a version bump (e.g., `/v2/api/...`) and a migration note.

### Communication
- Use PR descriptions to reference the section of the contract that changed.
- Tag the other developer in PR comments for awareness.
- If urgent, send a brief Slack/Teams message summarising the change.

### Git Workflow (recommended)
```
main
│
├─ feature/backend‑incident‑api
│   └─ work on FastAPI implementation
│
├─ feature/frontend‑incident‑ui
│   └─ work on Next.js pages & mock API client
│
└─ integration‑sync
    └─ occasional branch to resolve contract mismatches
```
- Merge to `main` via PR only after both sides have signed off.
- Rebase frequently on `main` to avoid long‑running divergent branches.

---
*Last updated: 2026‑09‑28*
