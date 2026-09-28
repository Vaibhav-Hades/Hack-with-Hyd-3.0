# app/models/verification_event.py
"""VerificationEvent model definition (placeholder)."""

from sqlalchemy import Column, String, DateTime, Enum as SAEnum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from sqlalchemy.orm import relationship
from app.core.database import Base

from enum import Enum as PyEnum

class VerificationStatus(str, PyEnum):
    pending = "pending"
    completed = "completed"
    failed = "failed"

class VerificationEvent(Base):
    __tablename__ = "verification_events"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    incident_id = Column(UUID(as_uuid=True), ForeignKey("incidents.id"), nullable=False)
    description = Column(String, nullable=False)
    status = Column(SAEnum(VerificationStatus), nullable=False, default=VerificationStatus.pending)
    timestamp = Column(DateTime, default=datetime.utcnow)

    incident = relationship("Incident", backref="verification_events")
