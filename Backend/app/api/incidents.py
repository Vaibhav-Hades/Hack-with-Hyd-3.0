# Backend/app/api/incidents.py

"""Incidents API router.
Provides endpoints defined in Docs/API_CONTRACT.md.
For now, returns stub/mock data matching the schema.
"""

from fastapi import APIRouter, Depends
from typing import List

from app.schemas.incident import IncidentRead, IncidentCreate, IncidentAnalysisResponse
from app.services.incident_service import IncidentService

router = APIRouter()

@router.get("/incidents", response_model=List[IncidentRead])
async def list_incidents(service: IncidentService = Depends()):
    return await service.list_incidents()

@router.get("/incidents/{incident_id}", response_model=IncidentRead)
async def get_incident(incident_id: str, service: IncidentService = Depends()):
    return await service.get_incident(incident_id)

@router.post("/incidents/analyze", response_model=IncidentAnalysisResponse)
async def analyze_incident(payload: IncidentCreate, service: IncidentService = Depends()):
    return await service.analyze_incident(payload)
