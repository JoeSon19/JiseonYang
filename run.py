"""
Production entry point for the Flask application
This file handles both development and production environments
"""
import os
from main import app

if __name__ == '__main__':
    # Development server
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
else:
    # Production WSGI
    application = app