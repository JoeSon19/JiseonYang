#!/usr/bin/env python3
"""
WSGI entry point for production deployment with Gunicorn
"""

import os
import sys
import logging
from main import app, init_db

# Configure logging for production
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)

def create_application():
    """Create and configure the Flask application for production"""
    logger.info("Initializing application for production deployment")
    
    try:
        # Initialize database
        with app.app_context():
            init_db()
            logger.info("Database initialization completed")
    except Exception as e:
        logger.warning(f"Database initialization warning: {str(e)}")
        logger.info("Application will continue without database initialization")
    
    return app

# Create application instance for Gunicorn
application = create_application()

# Create the application instance
application = create_application()

if __name__ == "__main__":
    # For development server
    port = int(os.environ.get('PORT', 5000))
    host = os.environ.get('HOST', '0.0.0.0')
    application.run(host=host, port=port, debug=False)