#!/usr/bin/env python3
"""
Simple, clean deployment startup script for Flask application.
This script avoids process conflicts and provides quick health check endpoints.
"""

import os
import logging
from main import app, init_db

# Configure logging for deployment
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    """Clean startup function for deployment"""
    logger.info("Starting application deployment...")
    
    # Initialize database
    try:
        init_db()
        logger.info("Database initialized successfully")
    except Exception as e:
        logger.warning(f"Database initialization warning: {str(e)}")
        logger.info("Continuing without database...")
    
    # Get single port configuration from environment
    port = int(os.environ.get('PORT', 5000))
    host = '0.0.0.0'
    
    logger.info(f"Starting Flask server on {host}:{port}")
    logger.info("Health check endpoints: /health and /ping")
    logger.info("Application ready for deployment")
    
    # Start with production-ready configuration
    app.run(
        host=host,
        port=port,
        debug=False,
        threaded=True,
        use_reloader=False
    )

if __name__ == '__main__':
    main()