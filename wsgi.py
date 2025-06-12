"""
WSGI entry point for production deployment
"""
from main import app
import logging

if __name__ == "__main__":
    # This is for production WSGI servers
    logging.basicConfig(level=logging.INFO)
    app.run()
else:
    # Configure logging for production
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(name)s %(message)s'
    )