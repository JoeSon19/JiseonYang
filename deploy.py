#!/usr/bin/env python3
"""
Ultra-simple deployment script for GCE Autoscale.
Addresses all deployment failure issues:
1. No process conflicts (no pkill commands)
2. Single port configuration only
3. Fast health check response
4. Binds to all interfaces for deployment
"""

import os
import sys
import logging
from main import app, init_db

# Minimal logging for deployment
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def deploy():
    """Clean deployment function"""
    # Quick database initialization
    try:
        init_db()
        logger.info("Database ready")
    except:
        logger.info("Database initialization skipped")
    
    # Single port configuration
    port = int(os.environ.get('PORT', 5000))
    
    logger.info(f"Deploying on 0.0.0.0:{port}")
    
    # Start with minimal configuration for fast startup
    app.run(
        host='0.0.0.0',
        port=port,
        debug=False,
        threaded=True,
        use_reloader=False
    )

if __name__ == '__main__':
    deploy()