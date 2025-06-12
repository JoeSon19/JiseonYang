import os

class Config:
    # Use environment variable for SECRET_KEY or fallback to a default for development
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    
    # Database configuration with error handling
    DATABASE_URL = os.environ.get('DATABASE_URL')
    if DATABASE_URL:
        # Handle postgres:// vs postgresql:// URL schemes
        if DATABASE_URL.startswith('postgres://'):
            DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)
        SQLALCHEMY_DATABASE_URI = DATABASE_URL
    else:
        # Fallback for development (SQLite)
        SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # CSRF protection
    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = os.environ.get('WTF_CSRF_SECRET_KEY', 'dev-csrf-key-change-in-production')
    
    # Production environment settings
    ENV = os.environ.get('FLASK_ENV', 'production')
    DEBUG = False
    TESTING = False
    
    # Server configuration
    HOST = '0.0.0.0'
    PORT = int(os.environ.get('PORT', 5000))
