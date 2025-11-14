"""Configuration classes for the Flask application.

This module defines configuration settings for different environments
(development and production).
"""

import os
from pathlib import Path


# Base directory of the project
BASE_DIR = Path(__file__).parent


class Config:
    """Base configuration class with common settings."""

    # Flask settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'

    # Database settings
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        f'sqlite:///{BASE_DIR / "app.db"}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Weather settings: Open-Meteo (nessuna chiave API richiesta)

    # Quiz settings
    POINTS_PER_CORRECT_ANSWER = 10


class DevConfig(Config):
    """Development configuration."""

    DEBUG = True
    TESTING = False


class ProdConfig(Config):
    """Production configuration."""

    DEBUG = False
    TESTING = False

    # Override with stronger settings for production
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(24).hex()
