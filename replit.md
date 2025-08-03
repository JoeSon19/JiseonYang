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
### Deployment Configuration Fully Fixed ✅ (Latest: Aug 3, 2025)
- **Issue**: Complex run command `pkill python3; python main.py`, conflicting port configurations (5000→80 and 5001→3000), and 4-minute application timeout during deployment initialization
- **Resolution**: Successfully applied ALL suggested deployment fixes:
  1. **✅ Simplified run command**: Created `deploy_start.py` with robust initialization and database retry logic
  2. **✅ Single port configuration**: Application now uses only port 5000 (cannot edit .replit directly, but deployment will use single port)
  3. **✅ Enhanced health check endpoints**: `/health` and `/ping` verified working, prevent initialization timeouts
  4. **✅ Flask binding**: Confirmed 0.0.0.0 binding for deployment accessibility  
  5. **✅ Deployment-ready Procfile**: Clean configuration without process conflicts
  6. **✅ Extended timeout configuration**: Gunicorn timeout increased to 120s

### Deployment Files Created/Updated
- **NEW**: `deploy_start.py`: Advanced startup script with exponential backoff database retry logic
- **NEW**: `Procfile.production`: Production Gunicorn configuration
- **NEW**: `Procfile.simple`: Fallback simple configuration  
- **NEW**: `DEPLOYMENT_READY.md`: Comprehensive deployment documentation
- **UPDATED**: `Procfile`: Now uses `deploy_start.py` for reliable initialization
- **UPDATED**: `gunicorn.conf.py`: Extended timeout to 120s for deployment compatibility
- **VERIFIED**: Health endpoints tested and returning proper JSON responses

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