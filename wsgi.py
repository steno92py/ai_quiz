"""WSGI entry point for PythonAnywhere deployment.

This module creates the Flask application instance for production deployment.
PythonAnywhere expects an 'application' object to be defined.
"""

import sys
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from project .env file (explicit path)
project_home = Path(__file__).parent
dotenv_path = project_home / '.env'
load_dotenv(dotenv_path=dotenv_path)

# Add the project directory to the Python path
if str(project_home) not in sys.path:
    sys.path.insert(0, str(project_home))

from app import create_app
from config import ProdConfig

# Create the application instance for WSGI
application = create_app(ProdConfig)

if __name__ == '__main__':
    # For local testing only
    application.run(debug=False)
