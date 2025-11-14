"""Quiz blueprint for quiz functionality."""

from flask import Blueprint

quiz_bp = Blueprint('quiz', __name__)

from app.quiz import routes
