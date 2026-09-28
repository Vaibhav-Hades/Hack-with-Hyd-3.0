# UI_SPECIFICATION.md

## Visual Theme (Dark‑First)
| Element | Color (Hex) | Purpose |
|---------|------------|---------|
| Background | `#080B12` | Main canvas, reduces eye‑strain for long monitoring sessions |
| Card / Panel | `#0F141D` | Contain incident cards, memory panels, and details |
| Border / Divider | `#202938` | Subtle separation without harsh contrast |
| Primary AI / Hindsight Accent | `#22D3EE` | Highlights AI‑generated suggestions, memory tags |
| Critical / Error | `#EF4444` | Immediate attention (failed fix, severe incident) |
| Warning | `#F59E0B` | Cautionary notices (partial fix, pending remediation) |
| Success | `#22C55E` | Successful outcomes (fix applied, verification passed) |
| Primary Text | `#F8FAFC` | Default readable text on dark background |
| Muted Text | `#94A3B8` | Secondary information, timestamps, IDs |

## Navigation Structure
- **Dashboard** – Overview of active incidents, severity distribution, and recent memory highlights.
- **Active Incidents** – List of currently open incidents with quick status badges.
- **Incident History** – Browse past incidents with filters (service, severity, date).
- **Incident Detail** – Full view of a selected incident, including timeline, investigation notes, and AI suggestions.
- **Resolution Memory** – Panel showing past resolution attempts for the incident.
- **Remediation Memory** – Permanent remediation actions linked to the incident.
- **Recurrence Patterns** – Detected patterns and similarity scores.
- **Services** – Service catalog with owners and health indicators.

## Page Specifications
### Dashboard
- **Header**: App name, global search, user avatar placeholder.
- **Severity Summary Cards** (critical, high, medium, low) using Success/Critical colors.
- **Live Incident Feed**: Card list of open incidents sorted by severity. Each card displays:
  - Incident ID, title, service badge, severity color.
  - Real‑time status badge (e.g., `Investigating`).
  - **Memory Summary** snippet (e.g., "2 historical incidents recalled – 1 remediation pending").
- **Quick AI Insight**: Small panel showing top‑ranked recent AI recommendation.

### Incident Investigation (Detail Page)
- **Top Bar**: Incident metadata (ID, title, service, severity badge, timestamps).
- **Tabs**: `Overview`, `Investigation`, `Resolution`, `Remediation`, `Verification`, `Memory`.
- **Memory Panel (right side)**:
  - Section header "Hindsight Memory" with accent color.
  - List items:
    - "Related incidents: 3 (87% similarity)"
    - "Previous resolutions: 2 failed, 1 success"
    - "Remediation history: connection‑pool config"
  - **View Sources** button toggles a modal showing raw memory excerpts.
- **AI Copilot Chat** (bottom‑right overlay):
  - Prompt examples (buttons): "Why is this happening?", "What worked before?", "Is the remediation still valid?".
  - AI response displayed in a card with `Primary AI` accent.

### Resolution Memory Page
- Table of past attempts (`action`, `outcome`, `timestamp`).
- Outcome badge colored: red (failed), orange (partial), green (success).
- Filter by outcome.
- Link each attempt to the corresponding incident detail.

### Remediation Memory Page
- List of permanent remediation actions with columns:
  - Action description
  - Implemented date
  - Status badge (`pending` gray, `completed` green)
- Ability to view linked verification events.

### Recurrence Patterns Page
- Card list of detected patterns. Each card shows:
  - Pattern description
  - Severity impact color
  - Number of incidents linked
  - Last detected timestamp
  - **Similarity Slider** (visual cue of similarity for current incident).

### Services Page
- Table: Service name, owner, incident count, health indicator (green/yellow/red).
- Clicking a service filters the Dashboard and Incident History to that service.

## Core UI Components (Reusable)
- **Badge** – colored label for severity, status, outcome.
- **Card** – container with subtle shadow, rounded corners, uses `#0F141D` background.
- **Table** – consistent column layout, supports sorting and pagination.
- **Modal** – centered, dark overlay (`rgba(0,0,0,0.8)`), close button.
- **AI Memory Panel** – collapsible side drawer, uses accent color for headings.
- **Copilot Chat Bubble** – speech‑bubble style with AI accent, minimal animation on new messages.

## Interaction Principles
- **Context‑aware**: AI suggestions are always tied to the currently selected incident.
- **No generic chatbot UI**: All AI output appears in designated panels, not a free‑form chat window.
- **Minimal animations**: Subtle hover effects, fade‑in for panel reveals; no distracting motion.
- **Accessibility**: Contrast complies with WCAG AA; focus outlines visible; keyboard navigation supported.

## Exclusions
- No social features (comments, likes).
- No real‑time streaming dashboards – data updates via polling of the API.
- No heavy 3D or gaming‑style graphics.

*Last updated: 2026‑09‑28*
