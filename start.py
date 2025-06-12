#!/usr/bin/env python3
"""
Simplified startup script for deployment
Ensures clean process startup without conflicts
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

def main():
    """Clean startup process for deployment"""
    try:
        # Initialize database
        logger.info("Initializing database...")
        init_db()
        
        # Get port from environment
        port = int(os.environ.get('PORT', 5000))
        
        logger.info(f"Starting Flask application on 0.0.0.0:{port}")
        
        # Start the application
        app.run(
            host='0.0.0.0',
            port=port,
            debug=False,
            threaded=True,
            use_reloader=False
        )
        
    except Exception as e:
        logger.error(f"Startup failed: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    main()