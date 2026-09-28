# alembic/env.py
"""Alembic environment configuration.
This file sets up the migration context using the project's async settings.
For simplicity, it runs migrations in offline mode using the DATABASE_URL
from the backend config. In a real project, you'd configure async migrations
or use a sync engine.
"""

from __future__ import with_statement
from logging.config import fileConfig

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from alembic import context
from sqlalchemy import engine_from_config, pool

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata

# we import the project's Base metadata
from app.core.database import Base  # noqa: E402
import app.models  # noqa: E402

target_metadata = Base.metadata

# get database URL from settings (via environment variables)
try:
    from app.core.config import settings  # noqa: E402
except Exception:
    settings = None

# If settings is None or DATABASE_URL is not set, fall back to env or alembic config
if not getattr(settings, "DATABASE_URL", None):
    import os
    fallback_url = os.getenv('DATABASE_URL') or config.get_main_option('sqlalchemy.url')
    class _FallbackSettings:
        DATABASE_URL = fallback_url
    settings = _FallbackSettings()

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.
    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well. By skipping the Engine creation
    we don't even need a DB driver to be available.
    """
    url = settings.DATABASE_URL
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_name="postgresql",
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.
    In this scenario we need to create an Engine
    and associate a connection with the context.
    """
    configuration = config.get_section(config.config_ini_section)
    configuration["sqlalchemy.url"] = settings.DATABASE_URL

    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
