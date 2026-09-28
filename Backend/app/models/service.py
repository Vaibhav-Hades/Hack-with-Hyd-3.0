# app/models/service.py
"""Service model definition."""

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.core.database import Base

class Service(Base):
    __tablename__ = "services"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False, unique=True)
