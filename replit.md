# Professor Website Project

## Project Overview
A professional website for a professor using Flask and Vanilla JS, featuring basic information, research, courses, and a contact form with PostgreSQL database integration.

## Project Architecture
- **Backend**: Flask (Python 3.11)
- **Frontend**: Vanilla JS, HTML5, CSS3
- **Database**: PostgreSQL (development and production ready)
- **Deployment**: Replit Autoscale compatible
- **WSGI Server**: Gunicorn for production

## Current Features
- Home page with professor information
- Research showcase
- Publications listing
- Contact form with database storage
- Health check endpoints for deployment
- Multiple entry points for flexibility

## Recent Changes (August 2025)
### Deployment Configuration Fixed ✅ (Latest: Aug 3, 2025)
- **Issue**: Complex run command, conflicting port configurations, and missing health checks causing deployment failures
- **Resolution**: Applied comprehensive deployment fixes:
  1. **Simplified run command**: Eliminated complex `pkill python3; python main.py` command
  2. **Single port configuration**: Removed conflicting 5001→3000 port mapping for GCE Autoscale compliance
  3. **Enhanced health check endpoints**: Improved `/health` and `/ping` endpoints to prevent initialization timeout
  4. **Production-ready Flask configuration**: Optimized for deployment with proper error handling
  5. **Multiple deployment entry points**: Created production-ready startup scripts

### Deployment Files Created/Updated
- `start.py`: Clean startup script for simple deployment
- `wsgi.py`: Production WSGI entry point for Gunicorn
- `gunicorn.conf.py`: Optimized server configuration for Replit Autoscale
- `DEPLOYMENT.md`: Comprehensive deployment guide and troubleshooting
- Enhanced `main.py`: Improved health checks and deployment configuration
- Health endpoints: `/health` (comprehensive with database status) and `/ping` (simple readiness check)

## File Structure
```
├── main.py              # Primary Flask application
├── wsgi.py             # WSGI production entry point
├── Procfile            # Deployment configuration (Gunicorn)
├── Procfile.simple     # Backup deployment configuration
├── gunicorn.conf.py    # Production server configuration
├── config.py           # Application configuration
├── models.py           # Database models
├── forms.py            # WTForms for contact form
├── static/             # CSS, JS, images
├── templates/          # HTML templates
└── instance/           # SQLite database (development)
```

## Environment Variables
- `DATABASE_URL`: PostgreSQL connection string
- `SECRET_KEY`: Flask secret key
- `WTF_CSRF_SECRET_KEY`: CSRF protection
- `PORT`: Deployment port (defaults to 5000)

## Deployment Status
**Ready for Replit Autoscale Deployment** ✅
- All deployment issues resolved
- Health check endpoints functional
- Production-ready WSGI configuration
- Single port configuration compliance
- Clean run commands without process conflicts

## User Preferences
*None specified yet*

## Technical Notes
- Uses Flask-SQLAlchemy for database ORM
- WTForms for form validation
- Bootstrap for responsive design
- Health checks prevent deployment timeouts
- Graceful error handling throughout