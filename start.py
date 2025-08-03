#!/usr/bin/env python3
"""
Simple startup script for deployment
This provides a clean entry point without process conflicts
"""

import os
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    """Main startup function"""
    try:
        # Import and initialize the application
        from main import app, init_db
        
        # Initialize database
        init_db()
        
        # Get port from environment
        port = int(os.environ.get('PORT', 5000))
        host = '0.0.0.0'
        
        logger.info(f"Starting application on {host}:{port}")
        logger.info("Health endpoints available: /health and /ping")
        
        # Start the application
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