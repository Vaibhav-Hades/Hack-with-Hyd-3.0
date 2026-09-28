# MEMORY_ARCHITECTURE.md

## Overview
RESOLVE stores **two complementary layers of data**:
- **Structured deterministic state** in PostgreSQL (incident metadata, service catalog, remediation records, verification events). 
- **Long‑term organizational memory** in Hindsight (unstructured narratives, hypotheses, outcomes, lessons).

The memory layer is the core product capability – it enables the agent to *remember* what has happened and *reason* over that history.

---

## Memory Categories

### 1. Incident Memory
- **What is stored**: Raw incident report – title, description, timestamps, service, severity, initial alerts.
- **Why it matters**: Serves as the anchor for all subsequent reasoning; provides context for what the incident is about.
- **Example**:
```json
{"id":"INC-482","title":"Database connection‑pool exhaustion","description":"...","severity":"high","service_id":"svc-01","opened_at":"2026‑09‑20T14:32:00Z"}
```
- **When retained**: Immediately upon `POST /api/incidents/analyze`.
- **When recalled**: Every time the agent processes the incident (analysis, remediation, verification).

### 2. Investigation Memory
- **What is stored**: Collected evidence – log snippets, metrics, hypothesis statements, diagnostic commands.
- **Why it matters**: Captures the investigative trail; useful for future engineers to see *how* the root cause was discovered.
- **Example**:
```json
{"incident_id":"INC-482","hypotheses":["connection‑pool limit too low","sudden traffic spike"],"evidence":["pool size=50","requests/sec=500"]}
```
- **When retained**: After each investigative action (e.g., a log query) and when the incident reaches a *root‑cause* decision.
- **When recalled**: When the agent suggests next investigative steps or when a similar incident is later examined.

### 3. Resolution Memory
- **What is stored**: All attempted fixes with outcomes (failed, partial, success), timestamps, and context notes.
- **Why it matters**: Enables pattern detection of what works or fails for certain symptom clusters.
- **Example**:
```json
{"incident_id":"INC-482","attempts":[{"id":"att-01","action":"restart service","outcome":"failed"},{"id":"att-02","action":"increase timeout","outcome":"partial"}]}
```
- **When retained**: Immediately after each attempt is recorded by the backend.
- **When recalled**: During analysis of a new incident to surface prior attempts.

### 4. Remediation Memory
- **What is stored**: Permanent changes applied to prevent recurrence – config changes, code patches, architectural upgrades.
- **Why it matters**: Differentiates *temporary fixes* from *lasting solutions*; crucial for learning.
- **Example**:
```json
{"incident_id":"INC-482","remediation":"Set connection‑pool max=200","implemented_at":"2026‑09‑22T09:15:00Z"}
```
- **When retained**: After a successful resolution is marked permanent.
- **When recalled**: When checking if existing remediations cover a new incident.

### 5. Verification Memory
- **What is stored**: Post‑remediation verification steps and their results (e.g., smoke tests, monitoring alerts).
- **Why it matters**: Confirms that a remediation actually fixed the underlying problem.
- **Example**:
```json
{"remediation_id":"rem-01","verification":"run load test","result":"pass","verified_at":"2026‑09‑23T11:00:00Z"}
```
- **When retained**: After verification is performed.
- **When recalled**: During recurrence detection to ensure the verification was adequate.

### 6. Recurrence Memory
- **What is stored**: Detected patterns of repeat incidents, similarity scores, and linked incident IDs.
- **Why it matters**: Drives proactive alerts and knowledge‑base suggestions.
- **Example**:
```json
{"pattern_id":"pat-07","description":"connection‑pool exhaustion under load","incident_ids":["INC-421","INC-482"],"similarity":0.87}
```
- **When retained**: After the pattern detection job runs (periodic or on‑demand).
- **When recalled**: When a new incident is opened; the agent checks for matching patterns.

---

## Hindsight Lifecycle (Memory Operations)
```
RETAIN    → Store new raw data (incident, attempts, remediation, verification) in Hindsight.
RECALL    → Retrieve relevant historical memories for a given incident.
REFLECT   → Agent + LLM reason over recalled memories + current evidence.
RECOMMEND → Produce actionable suggestions for the engineer.
RESOLVE   → Apply recommended action; outcome stored.
RETAIN OUTCOME → Persist outcome back into Hindsight (and PostgreSQL).
VERIFY    → Run verification steps; store results.
LEARN     → Pattern extraction & recurrence detection; update Recurrence Memory.
```

**Key Principle**: Hindsight is *not* a generic key‑value store. It provides semantic search, similarity scoring, and narrative retrieval that the LLM can consume, while PostgreSQL stores the canonical relational view.
