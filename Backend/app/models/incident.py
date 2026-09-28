# app/models/incident.py
"""Incident model definition."""

from sqlalchemy import Column, String, Text, DateTime, Enum as SAEnum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from sqlalchemy.orm import relationship

from app.core.database import Base
from enum import Enum as PyEnum
from .service import Service

class IncidentStatus(str, PyEnum):
    open = "open"
    investigating = "investigating"
    resolved = "resolved"
    closed = "closed"

class IncidentSeverity(str, PyEnum):
    low = "low"
    medium = "medium"
    high = "high"
    critical = "critical"

class Incident(Base):
    __tablename__ = "incidents"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    severity = Column(SAEnum(IncidentSeverity), nullable=False)
    status = Column(SAEnum(IncidentStatus), nullable=False, default=IncidentStatus.open)
    opened_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    service_id = Column(UUID(as_uuid=True), ForeignKey("services.id"), nullable=False)

    service = relationship("Service", backref="incidents")
