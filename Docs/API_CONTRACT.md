# API_CONTRACT.md

## Overview
This document defines the initial REST API contract between the **Frontend** (Next.js) and the **Backend** (FastAPI). All endpoints return JSON and use standard HTTP status codes. The contract is version‑agnostic but should remain stable; any change must be reflected in this document and communicated to the other team.

---

## Endpoints

### `GET /api/incidents`
- **Purpose**: List all incidents visible to the requester.
- **Request**: No body. Optional query parameters:
  - `status` (string) – filter by `open`, `closed`, `investigating`.
  - `service_id` (UUID) – filter incidents related to a service.
- **Response (200)**:
```json
[
  {
    "id": "uuid",
    "title": "string",
    "severity": "low|medium|high|critical",
    "status": "open|investigating|resolved|closed",
    "opened_at": "ISO8601 timestamp",
    "service_id": "uuid"
  }
]
```
- **Errors**:
  - `401 Unauthorized` – if auth required (future).
  - `500 Internal Server Error` – unexpected failure.

### `GET /api/incidents/{id}`
- **Purpose**: Retrieve detailed information for a single incident.
- **Path Params**:
  - `id` (UUID) – incident identifier.
- **Response (200)**:
```json
{
  "id": "uuid",
  "title": "string",
  "description": "string",
  "severity": "low|medium|high|critical",
  "status": "open|investigating|resolved|closed",
  "opened_at": "ISO8601",
  "updated_at": "ISO8601",
  "service_id": "uuid",
  "root_cause": "string|null",
  "current_step": "string"
}
```
- **Errors**: `404 Not Found`, `401 Unauthorized`, `500`.

### `POST /api/incidents/analyze`
- **Purpose**: Submit a new incident (or an update) for AI analysis.
- **Request Body**:
```json
{
  "title": "string",
  "description": "string",
  "severity": "low|medium|high|critical",
  "service_id": "uuid"
}
```
- **Response (202)** – analysis is asynchronous; returns a job identifier.
```json
{ "analysis_id": "uuid", "status": "queued" }
```
- **Later** the frontend can poll `GET /api/incidents/{id}/memory` for results.
- **Errors**: `400 Bad Request`, `422 Unprocessable Entity`.

### `GET /api/incidents/{id}/memory`
- **Purpose**: Retrieve Hindsight‑derived memory relevant to the incident.
- **Response (200)**:
```json
{
  "incident_id": "uuid",
  "related_incidents": ["uuid", "uuid"],
  "summary": "string",
  "memory_sources": ["Hindsight", "PostgreSQL"]
}
```
- **Errors**: `404`, `500`.

### `GET /api/incidents/{id}/resolution`
- **Purpose**: Fetch resolution attempts and their outcomes.
- **Response (200)**:
```json
[
  {
    "attempt_id": "uuid",
    "description": "string",
    "outcome": "failed|partial|success",
    "timestamp": "ISO8601"
  }
]
```

### `GET /api/incidents/{id}/remediation`
- **Purpose**: Get permanent remediation actions associated with the incident.
- **Response (200)**:
```json
[
  {
    "remediation_id": "uuid",
    "action": "string",
    "implemented_at": "ISO8601",
    "status": "pending|completed"
  }
]
```

### `GET /api/patterns`
- **Purpose**: List detected recurrence patterns across incidents.
- **Response (200)**:
```json
[
  {
    "pattern_id": "uuid",
    "description": "string",
    "incident_ids": ["uuid", "uuid"],
    "severity": "high",
    "last_detected": "ISO8601"
  }
]
```

### `GET /api/services`
- **Purpose**: Enumerate services/components tracked by RESOLVE.
- **Response (200)**:
```json
[
  { "id": "uuid", "name": "string", "owner": "string" }
]
```

---

## Versioning & Compatibility
- The contract is **stable** for the MVP. Any breaking change requires:
  1. Update this file.
  2. Increment a documented API version (e.g., `/v2/api/...`).
  3. Notify the frontend team via the **Integration Rules**.

## Mock Data
Developers may use the JSON examples above as mock responses while the backend is under construction.

---

*Last updated: 2026‑09‑28*
