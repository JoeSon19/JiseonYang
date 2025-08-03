#!/usr/bin/env python3
"""
Deployment startup script for the professor website
Ensures proper initialization and graceful startup for deployment
"""

import os
import sys
import time
import logging
from main import app, init_db

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def wait_for_database():
    """Wait for database to be ready with exponential backoff"""
    max_retries = 10
    retry_count = 0
    
    while retry_count < max_retries:
        try:
            init_db()
            logger.info("Database initialized successfully")
            return True
        except Exception as e:
            retry_count += 1
            wait_time = min(2 ** retry_count, 30)  # Exponential backoff, max 30s
            logger.warning(f"Database initialization attempt {retry_count} failed: {str(e)}")
            if retry_count < max_retries:
                logger.info(f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
    
    logger.error("Database initialization failed after all retries")
    return False

def main():
    """Main deployment startup function"""
    logger.info("Starting deployment initialization...")
    
    # Initialize database with retry logic
    if not wait_for_database():
        logger.error("Failed to initialize database. Starting without database...")
    
    # Get deployment configuration
    port = int(os.environ.get('PORT', 5000))
    host = os.environ.get('HOST', '0.0.0.0')
    
    logger.info(f"Starting Flask server on {host}:{port}")
    logger.info("Health check endpoints available at /health and /ping")
    logger.info("Application ready for deployment")
    
    try:
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
    main()