# app/models/remediation.py
"""Remediation model definition (placeholder)."""

from sqlalchemy import Column, String, DateTime, Enum as SAEnum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from sqlalchemy.orm import relationship
from app.core.database import Base

from enum import Enum as PyEnum

class RemediationStatus(str, PyEnum):
    pending = "pending"
    completed = "completed"

class Remediation(Base):
    __tablename__ = "remediations"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    incident_id = Column(UUID(as_uuid=True), ForeignKey("incidents.id"), nullable=False)
    action = Column(String, nullable=False)
    implemented_at = Column(DateTime, nullable=True)
    status = Column(SAEnum(RemediationStatus), nullable=False, default=RemediationStatus.pending)

    incident = relationship("Incident", backref="remediations")
