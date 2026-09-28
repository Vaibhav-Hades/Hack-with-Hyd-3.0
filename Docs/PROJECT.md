# PROJECT.md

## Purpose
RESOLVE is an AI‑powered Incident Response Agent that **remembers** every incident, investigation, and remediation to improve future responses.

## Problem Solved
Engineering teams spend excessive time re‑investigating recurring incidents because knowledge is lost after a fix.  RESOLVE captures the full lifecycle of incidents and makes that knowledge instantly reusable.

## Target Users
- Site reliability engineers (SREs) and incident responders
- Platform engineering teams
- On‑call engineers who need rapid root‑cause insights

## Official Problem Mapping
- **Domain**: Incident Response Agent
- **Differentiator**: Persistent resolution, remediation, verification, and recurrence memory.

## Core Workflow
```
Incident → Investigation → Root Cause → Attempted Fixes →
[Failed | Partial | Successful] → Permanent Remediation →
Verification → Recurrence Detection → Organizational Learning
```

## Major Features (Phase‑1)
- Incident ingestion via API
- AI‑driven analysis using configurable LLMs
- Hindsight integration for long‑term memory
- Structured incident state stored in PostgreSQL
- UI for incident list, details, and memory panels (future)

## Role of Hindsight
Provides **long‑term, unstructured organizational memory** – recall of past incidents, hypotheses, fixes, and outcomes. It is not a replacement for the relational DB.

## Role of PostgreSQL
Holds deterministic application data: incident metadata, service catalog, remediation records, verification events, etc.

## Expected User Experience
- Engineers open an incident in the dashboard.
- The system immediately surfaces related historical incidents and outcomes.
- AI suggests next steps based on past successes/failures.

## Non‑Goals
- Real‑time monitoring or alerting platform
- Full‑blown ticketing system
- Deep dive UI visualizations (outside scope of foundation)

## Important Product Principles
- **Memory‑first**: Organizational memory is core, not optional.
- Provider‑agnostic LLM integration.
- Clear separation of concerns between frontend, backend, DB, and memory layers.
- Simplicity for a two‑person team.
