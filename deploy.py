"""
Deployment preparation script
Ensures all components are ready for production deployment
"""
import os
import sys
from main import app, db
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def check_environment():
    """Check if all required environment variables are set"""
    required_vars = []
    
    # Check optional vars with fallbacks
    optional_vars = {
        'SECRET_KEY': 'Uses fallback in development',
        'DATABASE_URL': 'Uses SQLite fallback',
        'PORT': 'Uses port 5000 as default'
    }
    
    logger.info("Environment Variables Check:")
    for var, description in optional_vars.items():
        value = os.environ.get(var)
        if value:
            logger.info(f"✓ {var}: Set")
        else:
            logger.info(f"- {var}: Not set ({description})")
    
    return len(required_vars) == 0

def test_database_connection():
    """Test database connectivity"""
    try:
        with app.app_context():
            from sqlalchemy import text
            result = db.session.execute(text('SELECT 1'))
            result.fetchone()
        logger.info("✓ Database connection: Working")
        return True
    except Exception as e:
        logger.error(f"✗ Database connection failed: {str(e)}")
        return False

def test_application_routes():
    """Test critical application routes"""
    with app.test_client() as client:
        try:
            # Test home page
            response = client.get('/')
            if response.status_code == 200:
                logger.info("✓ Home page: Working")
            else:
                logger.error(f"✗ Home page failed: {response.status_code}")
                return False
            
            # Test health check
            response = client.get('/health')
            if response.status_code == 200:
                logger.info("✓ Health check endpoint: Working")
            else:
                logger.error(f"✗ Health check failed: {response.status_code}")
                return False
            
            return True
        except Exception as e:
            logger.error(f"✗ Route testing failed: {str(e)}")
            return False

def main():
    """Run all deployment checks"""
    logger.info("Starting deployment readiness check...")
    
    checks = [
        ("Environment Variables", check_environment),
        ("Database Connection", test_database_connection),
        ("Application Routes", test_application_routes)
    ]
    
    all_passed = True
    for check_name, check_func in checks:
        logger.info(f"\n--- {check_name} ---")
        if not check_func():
            all_passed = False
    
    logger.info("\n" + "="*50)
    if all_passed:
        logger.info("🎉 All deployment checks PASSED!")
        logger.info("Application is ready for deployment.")
    else:
        logger.error("❌ Some checks FAILED!")
        logger.error("Please fix the issues before deploying.")
        sys.exit(1)

if __name__ == "__main__":
    main()