# DATA_MODEL.md

## Conceptual PostgreSQL Schema

The relational model stores **deterministic** incident data that can be queried efficiently. Below is a high‑level description; actual migrations will be added later.

### tables

#### `services`
- `id` UUID PK
- `name` VARCHAR(100) – human readable service name
- `owner` VARCHAR(100) – team or person responsible
- `created_at` TIMESTAMP
- `updated_at` TIMESTAMP

#### `incidents`
- `id` UUID PK
- `title` VARCHAR(200)
- `description` TEXT
- `severity` ENUM('low','medium','high','critical')
- `status` ENUM('open','investigating','resolved','closed')
- `opened_at` TIMESTAMP
- `closed_at` TIMESTAMP NULL
- `service_id` UUID FK → `services.id`
- `root_cause` TEXT NULL
- `current_step` VARCHAR(50) – e.g., "investigating", "remediation"

#### `incident_attempts`
- `id` UUID PK
- `incident_id` UUID FK → `incidents.id`
- `action` TEXT – description of the fix attempt
- `outcome` ENUM('failed','partial','success')
- `performed_at` TIMESTAMP

#### `remediations`
- `id` UUID PK
- `incident_id` UUID FK → `incidents.id`
- `action` TEXT – permanent change (config, code, process)
- `implemented_at` TIMESTAMP
- `status` ENUM('pending','completed')

#### `verification_events`
- `id` UUID PK
- `remediation_id` UUID FK → `remediations.id`
- `verification_step` TEXT – e.g., "run load test"
- `result` ENUM('pass','fail')
- `verified_at` TIMESTAMP

#### `incident_patterns`
- `id` UUID PK
- `description` TEXT – human readable pattern name
- `severity` ENUM('low','medium','high','critical')
- `last_detected` TIMESTAMP

#### `pattern_incidents` (junction table)
- `pattern_id` UUID FK → `incident_patterns.id`
- `incident_id` UUID FK → `incidents.id`

### Relationships
- **Service 1‑* Incident** – each incident belongs to a service.
- **Incident 1‑* Incident_Attempt** – multiple fix attempts per incident.
- **Incident 1‑* Remediation** – zero or more permanent actions.
- **Remediation 1‑* Verification_Event** – verifications tied to a remediation.
- **Incident *‑* Incident_Pattern** via `pattern_incidents` – many‑to‑many linking of incidents to detected patterns.

### Distinction from Hindsight
All columns above are **structured**, searchable with SQL, and used for core application state. Narrative details, hypothesis text, and similarity scoring live in **Hindsight** and are linked via the incident UUIDs.

---

*Last updated: 2026‑09‑28*
