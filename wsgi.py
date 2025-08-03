"""
WSGI entry point for production deployment
This file provides the WSGI application object that Gunicorn can use
"""

import os
import sys
import logging

# Add the project directory to Python path
sys.path.insert(0, os.path.dirname(__file__))

from main import app, init_db

# Configure logging for production
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize database on startup
try:
    init_db()
    logger.info("Database initialized successfully")
except Exception as e:
    logger.error(f"Database initialization error: {str(e)}")

# WSGI application object
application = app

if __name__ == "__main__":
    # For direct execution (development)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)