"""
WSGI entry point for production deployment
"""
from main import app, init_db
import logging
import os

# Configure logging for production
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize database on startup
init_db()

if __name__ == "__main__":
    # This is for production WSGI servers like Gunicorn
    port = int(os.environ.get('PORT', 5000))
    logger.info(f"Starting WSGI application on port {port}")
    app.run(host='0.0.0.0', port=port, debug=False, threaded=True)

# Export app for WSGI servers
application = app