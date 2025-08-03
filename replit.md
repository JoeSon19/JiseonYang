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
### Deployment Configuration Fixed ✅
- **Issue**: Complex run command and conflicting port configurations causing deployment failures
- **Resolution**: Applied all suggested deployment fixes:
  1. **Simplified run command**: Changed from `pkill python3; python main.py` to clean Gunicorn deployment
  2. **Single port configuration**: Removed conflicting 5001→3000 port mapping
  3. **Health check endpoints**: Added `/health` and `/ping` for initialization timeout prevention
  4. **Production-ready configuration**: Optimized Gunicorn and Flask settings
  5. **Multiple Procfile options**: Primary (Gunicorn) and backup (direct Flask) configurations

### Deployment Files Created/Updated
- `Procfile`: Primary deployment with Gunicorn
- `Procfile.simple`: Backup deployment with direct Flask
- `gunicorn.conf.py`: Optimized for Autoscale deployment
- `wsgi.py`: Production WSGI entry point
- Health endpoints: `/health` (comprehensive) and `/ping` (simple)

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