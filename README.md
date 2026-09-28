# README.md

## RESOLVE – Incident response that remembers

### Project purpose
RESOLVE is an **AI‑powered Incident Response Agent** that captures the full lifecycle of incidents—investigation, root‑cause analysis, attempted fixes, permanent remediations, verification, and recurrence detection. By persisting this knowledge in a long‑term memory service (Hindsight) **and** a structured relational store (PostgreSQL), the system helps engineers resolve current incidents faster and prevents repeat failures.

### Problem being solved
Engineering teams repeatedly waste time re‑investigating similar incidents because knowledge is lost after a fix. RESOLVE stores that knowledge forever and surfaces it automatically during new incidents.

### Core workflow (high‑level)
```
Incident → Investigation → Root Cause → Attempted Fixes →
[Failed | Partial | Success] → Permanent Remediation →
Verification → Recurrence Detection → Organizational Learning
```

### Tech stack
- **Frontend**: Next.js (TypeScript) – dark‑first UI.
- **Backend**: FastAPI (Python) – REST API.
- **Database**: PostgreSQL – deterministic state.
- **Long‑term memory**: Hindsight – semantic/semantic memory.
- **LLM**: Configurable provider (OpenAI, Anthropic, etc.)

### Repository structure
```
/Docs                – project specifications & guidelines
/Frontend            – Next.js app (frontend)
/Backend             – FastAPI server (backend)
/DB                  – database scripts, migrations, seed data
/.gitignore          – ignore common artefacts
/.env.example        – environment variable placeholders
/AGENTS.md           – master instruction file for AI assistants
/README.md           – this overview
```

### Development setup (quick start)
1. **Clone the repo**
2. **Create a local env** from `.env.example`
3. **Frontend**:
   ```
   cd Frontend
   npm install
   npm run dev   # starts Next.js on http://localhost:3000
   ```
4. **Backend**:
   ```
   cd Backend
   pip install -r requirements.txt
   uvicorn main:app --reload   # runs FastAPI on http://localhost:8000
   ```
5. **Database**:
   - Install PostgreSQL locally or use a managed instance.
   - Apply migrations (to be added later).
6. **Hindsight**:
   - Obtain an API key and set `HINDSIGHT_API_KEY` in the env file.
   - No implementation yet – placeholders will be used.

### Documentation
All project specifications live in the `/Docs` folder. Future AI assistants must start by reading `AGENTS.md` which points to the relevant docs.

### Demo concept
The `Docs/DEMO_FLOW.md` file describes a synthetic end‑to‑end walkthrough that showcases memory‑first incident handling.

### Next steps
- Implement the FastAPI endpoints defined in `Docs/API_CONTRACT.md`.
- Scaffold the Next.js UI against the contract with mock data.
- Wire up Hindsight calls and LLM integration.

*Last updated: 2026‑09‑28*
