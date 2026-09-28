# ARCHITECTURE.md

## System Overview
RESOLVE consists of four primary layers:

1. **Frontend** – Next.js (TypeScript) UI.
2. **Backend** – FastAPI (Python) exposing a REST API.
3. **Structured Data Store** – PostgreSQL for deterministic state.
4. **Long‑Term Memory** – Hindsight service for unstructured incident memory.

The LLM provider is pluggable; the backend only needs an API key and model name.

### Component Diagram
```mermaid
flowchart LR
    subgraph FE[Frontend]
        UI[UI (Next.js)]
    end
    subgraph BE[Backend]
        API[FastAPI REST API]
        Agent[Incident‑Response Agent]
        LLM[LLM Provider]
    end
    subgraph DB[PostgreSQL]
        DB[(Structured DB)]
    end
    subgraph MEM[Hindsight]
        MEM[(Long‑Term Memory)]
    end
    UI -->|HTTP JSON| API
    API -->|CRUD| DB
    API -->|Analyze| Agent
    Agent -->|LLM Call| LLM
    Agent -->|Recall/Retain| MEM
    Agent -->|Store Outcome| DB
    Agent -->|Store Memory| MEM
    MEM -->|Recall| Agent
```

### Data Flow (Incident Lifecycle)
1. Engineer creates/opens an incident via UI.
2. Frontend calls `POST /api/incidents/analyze`.
3. Backend stores the incident in PostgreSQL.
4. Agent retrieves related memories from Hindsight (RECALL).
5. Agent invokes LLM to reason and produce recommendations.
6. Recommendations are returned to the frontend.
7. Outcomes (resolution, remediation, verification) are persisted to both PostgreSQL (structured) and Hindsight (unstructured) – **RETAIN OUTCOME**.

### Memory Flow
```
RETAIN → Hindsight
RECALL → Hindsight
REFLECT (Agent + LLM) → Recommendation
RESOLVE → Backend updates state
VERIFY → Hindsight stores verification event
LEARN → Patterns extracted for future RECALL
```

### Deployment Considerations
- Frontend can be deployed to Vercel (static export or server‑side rendering).
- Backend can be hosted on Render/Railway or any PaaS supporting Python.
- PostgreSQL is an external managed instance.
- Hindsight is accessed via its API; no local deployment required.

No additional micro‑services are introduced – the backend aggregates all backend responsibilities.
