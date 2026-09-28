# app/schemas/incident.py
"""Pydantic schemas for Incident resources."""

from pydantic import BaseModel, Field
from typing import Optional, List
from uuid import UUID
from datetime import datetime

class IncidentRead(BaseModel):
    id: UUID
    title: str
    severity: str
    status: str
    opened_at: datetime
    service_id: UUID

    class Config:
        orm_mode = True

class IncidentCreate(BaseModel):
    title: str
    description: Optional[str] = None
    severity: str
    service_id: UUID

class IncidentAnalysisResponse(BaseModel):
    analysis_id: UUID
    status: str = "queued"
