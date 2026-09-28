# app/api/memory.py
"""Memory API router placeholder."""

from fastapi import APIRouter, Depends
from typing import List

from app.schemas.memory import MemoryResponse
from app.services.incident_service import IncidentService

router = APIRouter()

@router.get("/incidents/{incident_id}/memory", response_model=MemoryResponse)
async def get_memory(incident_id: str, service: IncidentService = Depends()):
    # Placeholder implementation
    return await service.get_memory(incident_id)
