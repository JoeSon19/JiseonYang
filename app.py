"""
Alternative entry point for deployment compatibility
This ensures the Flask app can be started with various deployment commands
"""
from main import app, init_db
import os
import logging

# Configure production logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s %(message)s'
)

# Initialize database on import
init_db()

# Export app for deployment systems
application = app

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False, threaded=True)