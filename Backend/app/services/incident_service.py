# app/services/incident_service.py
"""Incident service layer stub implementation.
Provides placeholder data matching Pydantic schemas.
"""

import uuid
from typing import List
from datetime import datetime

from app.schemas.incident import IncidentRead, IncidentCreate, IncidentAnalysisResponse
from app.schemas.memory import MemoryResponse

class IncidentService:
    """Simple service with in‑memory placeholder data."""

    async def list_incidents(self) -> List[IncidentRead]:
        # Return empty list for now
        return []

    async def get_incident(self, incident_id: str) -> IncidentRead:
        # Return a dummy incident matching the schema
        return IncidentRead(
            id=uuid.UUID(incident_id) if incident_id else uuid.uuid4(),
            title="Sample Incident",
            severity="low",
            status="open",
            opened_at=datetime.utcnow(),
            service_id=uuid.uuid4(),
        )

    async def analyze_incident(self, payload: IncidentCreate) -> IncidentAnalysisResponse:
        # Return a placeholder analysis response
        return IncidentAnalysisResponse(
            analysis_id=uuid.uuid4(),
            status="queued",
        )

    async def get_memory(self, incident_id: str) -> MemoryResponse:
        # Return empty memory placeholder
        return MemoryResponse(
            incident_id=uuid.UUID(incident_id) if incident_id else uuid.uuid4(),
            related_incidents=[],
            summary=None,
            memory_sources=[],
        )
