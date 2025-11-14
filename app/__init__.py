"""Application factory for Flask app.

This module implements the application factory pattern, creating and
configuring the Flask application instance.
"""

import logging
from flask import Flask
from config import Config, DevConfig


def create_app(config_class=DevConfig):
    """Create and configure the Flask application.

    Args:
        config_class: Configuration class to use (default: DevConfig).

    Returns:
        Configured Flask application instance.
    """
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(config_class)

    # Log configuration info
    logger = logging.getLogger(__name__)
    logger.info("Meteo lato frontend: Open-Meteo (nessuna API key richiesta)")

    # Initialize extensions
    from app.extensions import db, login_manager
    db.init_app(app)
    login_manager.init_app(app)

    # Register user loader for Flask-Login
    from app.models import User

    @login_manager.user_loader
    def load_user(user_id: str):
        """Load user by ID for Flask-Login.

        Args:
            user_id: String representation of user ID.

        Returns:
            User object or None if not found.
        """
        return User.query.get(int(user_id))

    # Register blueprints
    from app.main import main_bp
    app.register_blueprint(main_bp)

    from app.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.quiz import quiz_bp
    app.register_blueprint(quiz_bp, url_prefix='/quiz')

    # Create database tables
    with app.app_context():
        db.create_all()

    return app
