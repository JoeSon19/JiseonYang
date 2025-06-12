"""
WSGI entry point for production deployment
"""
import os
import logging
from main import app, init_db

# Configure production logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)

# Initialize database on startup
try:
    init_db()
    logging.info("WSGI: Database initialized successfully")
except Exception as e:
    logging.error(f"WSGI: Database initialization failed: {str(e)}")

# Export application for WSGI servers
application = app

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    logging.info(f"WSGI: Starting application on 0.0.0.0:{port}")
    app.run(host='0.0.0.0', port=port, debug=False, threaded=True, use_reloader=False)