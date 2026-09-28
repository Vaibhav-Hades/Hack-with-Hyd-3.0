# app/core/database.py

"""SQLAlchemy async engine and session management.
Configuration is driven by environment variables via Settings.
"""

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

try:
    from app.core.config import settings
except Exception:  # Settings validation error when env missing
    settings = None

# Async PostgreSQL URL expects asyncpg driver, e.g., postgresql+asyncpg://...
if settings:
    DATABASE_URL = settings.DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")
    engine: AsyncEngine = create_async_engine(DATABASE_URL, echo=False, future=True)
    AsyncSessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)
else:
    engine = None
    AsyncSessionLocal = None

Base = declarative_base()
