#!/usr/bin/env python3
"""
Production startup script for deployment
This script provides a clean, simple way to start the Flask application
without complex shell commands that cause deployment conflicts.
"""

import os
import logging
import sys
from main import app, init_db

# Configure logging for production
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def start_application():
    """
    Start the Flask application with production-ready configuration
    """
    try:
        # Initialize database
        logger.info("Initializing database...")
        init_db()
        
        # Get port from environment variable for deployment compatibility
        port = int(os.environ.get('PORT', 5000))
        host = os.environ.get('HOST', '0.0.0.0')
        
        logger.info(f"Starting Flask server on {host}:{port}")
        logger.info("Health check endpoints available at /health and /ping")
        
        # Production-ready configuration
        app.run(
            host=host,
            port=port,
            debug=False,
            threaded=True,
            use_reloader=False
        )
        
    except Exception as e:
        logger.error(f"Failed to start application: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    start_application()