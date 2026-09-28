# app/core/config.py

"""Application configuration using Pydantic BaseSettings.
All values are read from environment variables; defaults are provided where appropriate.
"""

import pathlib
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

# Resolve project root (three levels up from this file)
PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[4]
load_dotenv(PROJECT_ROOT / ".env")

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=PROJECT_ROOT / ".env", env_file_encoding="utf-8")
    # Core settings
    DATABASE_URL: str = Field(..., env="DATABASE_URL")
    # Hindsight configuration
    HINDSIGHT_API_KEY: str = Field(default="", env="HINDSIGHT_API_KEY")
    HINDSIGHT_BANK_ID: str = Field(default="", env="HINDSIGHT_BANK_ID")
    HINDSIGHT_BASE_URL: str = Field(default="https://api.hindsight.ai", env="HINDSIGHT_BASE_URL")
    # LLM configuration (placeholders)
    LLM_API_KEY: str = Field(default="", env="LLM_API_KEY")
    LLM_MODEL: str = Field(default="gpt-4", env="LLM_MODEL")

# Instantiate settings – let validation errors surface naturally
settings = Settings()
