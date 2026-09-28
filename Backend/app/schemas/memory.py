# app/schemas/memory.py
"""Pydantic schema for memory endpoint response."""

from pydantic import BaseModel
from uuid import UUID
from typing import List, Optional

class MemoryResponse(BaseModel):
    incident_id: UUID
    related_incidents: List[UUID]
    summary: Optional[str] = None
    memory_sources: List[str]

    class Config:
        orm_mode = True
