# Backend/app/main.py

"""FastAPI application entry point.
It loads configuration, creates the database engine, and includes API routers.
"""

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.core.database import engine, Base
from app.api import incidents, memory, patterns, services

app = FastAPI(title="RESOLVE Backend API", version="0.1.0")

# CORS (allow all for development – can be restricted later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(incidents.router, prefix="/api", tags=["incidents"])
app.include_router(memory.router, prefix="/api", tags=["memory"])
app.include_router(patterns.router, prefix="/api", tags=["patterns"])
app.include_router(services.router, prefix="/api", tags=["services"])

# Startup / shutdown events to create DB tables (for dev only)
@app.on_event("startup")
async def on_startup():
    # Create tables if they do not exist – in production use Alembic migrations
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/health", tags=["health"])
async def health_check():
    return {"status": "ok"}
