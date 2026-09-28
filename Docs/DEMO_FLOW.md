# DEMO_FLOW.md

## End‑to‑End Demonstration (Synthetic)
The following walkthrough shows a realistic, **demo‑only** scenario that illustrates the core value‑proposition of RESOLVE – leveraging organizational memory to accelerate incident resolution.

### 1. Incident Occurs
- **Incident ID**: `INC-482`
- **Title**: *Database connection‑pool exhaustion*
- **Service**: `payments-api`
- **Severity**: `critical`
- **Timestamp**: `2026‑09‑20 14:32 UTC`
- Alert fires from monitoring (e.g., high latency, error spikes).

### 2. Engineer Opens the Incident
- Engineer logs into the RESOLVE dashboard (URL: `/incidents/INC-482`).
- The **Incident Detail** page loads with basic metadata.

### 3. Investigation Begins
- Engineer reviews logs via the UI and adds a hypothesis: *"Pool size too low for traffic surge"*.
- The UI sends these notes to the backend (stored in PostgreSQL).

### 4. Hindsight Recalls Historical Incident
- The backend calls **Hindsight** with the incident description.
- Hindsight returns a highly similar past incident:
  - **Historical ID**: `INC-421`
  - **Similarity**: `87%`
  - **Summary**: Same service, connection‑pool exhaustion under load.

### 5. Historical Resolution Attempts Displayed
- UI shows a **Resolution Memory** panel for `INC-421`:
  | Attempt | Action | Outcome |
  |--------|--------|---------|
  | 1 | Restart service | **FAILED** |
  | 2 | Increase timeout to 30s | **PARTIAL** |
  | 3 | Rollback to previous version | **SUCCESS** |
- Outcomes are colour‑coded (red, orange, green).

### 6. Previous Permanent Remediation Shown
- The **Remediation Memory** panel reveals a permanent fix that was applied after `INC-421`:
  - *"Set connection‑pool max=200 and enable auto‑scaling"*
  - Implemented on `2026‑09‑22`.

### 7. Historical Verification Displayed
- A **Verification** entry linked to the remediation shows:
  - Verification step: *Run load‑test for 10 min*
  - Result: **PASS**
  - Verified at `2026‑09‑23`.

### 8. Recurrence Detected
- The system detects that the same pattern has re‑appeared (connection‑pool exhaustion) and flags a **Recurrence Pattern**:
  - Pattern ID: `PAT‑07`
  - Description: *"Connection‑pool exhaustion under load"*
  - Incidents linked: `INC-421`, `INC-482`
  - Similarity: `87%`

### 9. AI‑Driven Recommendation
- The **AI Copilot** (via Hindsight + LLM) proposes next steps, displayed in the **AI Memory Panel**:
  1. *Verify current pool size (currently 100).*
  2. *Apply the proven permanent remediation (set max=200).*
  3. *Run the same verification load‑test.*
- The engineer clicks **Accept**; the backend records the chosen action as a new **incident_attempt** with status `pending`.

### 10. Outcome Recorded
- After the remediation is applied and verification passes, the backend:
  - Persists a **successful attempt** record.
  - Stores the outcome in **Hindsight** (`RETAIN OUTCOME`).
  - Updates the incident status to `resolved` in PostgreSQL.

### 11. Learning Loop
- The pattern detection job updates the **Recurrence Memory** to reflect the successful resolution, improving future RECALL scores.

---
*All data above is synthetic and intended solely for demonstration purposes.*

*Last updated: 2026‑09‑28*
