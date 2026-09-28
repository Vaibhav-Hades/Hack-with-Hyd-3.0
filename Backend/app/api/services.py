# app/api/services.py
"""Services API router placeholder."""

from fastapi import APIRouter
from typing import List

router = APIRouter()

@router.get("/services", response_model=List[dict])
async def list_services():
    # Placeholder returning empty list
    return []
