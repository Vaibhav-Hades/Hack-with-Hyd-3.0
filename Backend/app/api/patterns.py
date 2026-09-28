# app/api/patterns.py
"""Patterns API router placeholder."""

from fastapi import APIRouter
from typing import List

router = APIRouter()

@router.get("/patterns", response_model=List[dict])
async def list_patterns():
    # Placeholder returning empty list
    return []
