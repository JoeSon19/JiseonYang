"""
Production entry point for the Flask application
This file handles both development and production environments
"""
import os
import logging
from main import app, init_db

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s %(message)s'
)
logger = logging.getLogger(__name__)

def create_app():
    """Application factory for production deployment"""
    # Initialize database
    init_db()
    
    # Log startup information
    logger.info("Flask application initialized successfully")
    logger.info(f"Environment: {os.environ.get('FLASK_ENV', 'production')}")
    logger.info(f"Debug mode: {app.debug}")
    
    return app

if __name__ == '__main__':
    # Initialize and run the application
    application = create_app()
    
    # Get port from environment
    port = int(os.environ.get('PORT', 5000))
    
    logger.info(f"Starting Flask server on 0.0.0.0:{port}")
    application.run(host='0.0.0.0', port=port, debug=False, threaded=True)

# Export for WSGI servers
application = create_app()