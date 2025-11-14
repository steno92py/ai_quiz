"""Flask extensions initialization.

This module initializes Flask extensions that are used across the application.
Extensions are initialized here and then attached to the app in the factory.
"""

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


# Initialize SQLAlchemy
db = SQLAlchemy()

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Per favore, effettua il login per accedere a questa pagina.'
login_manager.login_message_category = 'warning'
