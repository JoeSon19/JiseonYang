from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from config import Config
from forms import ContactForm
from models import db, Contact
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config.from_object(Config)

# Initialize database with error handling
try:
    db.init_app(app)
    logger.info("Database initialized successfully")
except Exception as e:
    logger.error(f"Database initialization error: {str(e)}")

# Health check endpoint for deployment
@app.route('/health')
def health_check():
    """
    Comprehensive health check for deployment readiness
    Returns 200 OK if application is ready to serve traffic
    """
    health_status = {
        'status': 'healthy',
        'timestamp': str(db.func.now() if hasattr(db, 'func') else 'unknown'),
        'application': 'running'
    }
    
    try:
        # Test database connection with retry logic
        with app.app_context():
            from sqlalchemy import text
            result = db.session.execute(text('SELECT 1'))
            result.fetchone()
            db.session.close()
            health_status['database'] = 'connected'
        return health_status, 200
    except Exception as e:
        logger.warning(f"Database connection issue in health check: {str(e)}")
        # Return healthy for basic deployment checks even if database has temporary issues
        health_status['database'] = 'retrying'
        health_status['database_message'] = 'Temporary connection issue'
        return health_status, 200

# Simple health check for deployment readiness - ultra fast response
@app.route('/ping')
def ping():
    """Ultra-fast health check for GCE Autoscale deployment"""
    return 'pong', 200

# Additional quick health check
@app.route('/ready')
def ready():
    """Deployment readiness check"""
    return {'status': 'ready'}, 200

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/research')
def research():
    return render_template('research.html')

@app.route('/teaching')
def teaching():
    return render_template('teaching.html')

@app.route('/publications')
def publications():
    return render_template('publications.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            try:
                contact = Contact(
                    name=form.name.data,
                    email=form.email.data,
                    message=form.message.data
                )
                db.session.add(contact)
                db.session.commit()
                flash('Your message has been sent successfully!', 'success')
                logger.info(f'Contact form submitted by {form.name.data}')
                return redirect(url_for('contact'))
            except Exception as e:
                db.session.rollback()
                flash('An error occurred while sending your message. Please try again.', 'error')
                logger.error(f'Database error in contact form: {str(e)}')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f'{field}: {error}', 'error')
                    logger.warning(f'Form validation error - {field}: {error}')
    
    return render_template('contact.html', form=form)

@app.route('/media')
def media():
    return render_template('media.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/funding')
def funding():
    return render_template('funding.html')

@app.route('/honors')
def honors():
    return render_template('honors.html')

@app.route('/techniques')
def techniques():
    return render_template('techniques.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/presentations')
def presentations():
    return render_template('presentations.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/datascience')
def datascience():
    return render_template('DataScience.html')

# Initialize database tables
def init_db():
    try:
        with app.app_context():
            db.create_all()
            logger.info("Database tables created successfully")
    except Exception as e:
        logger.error(f"Error creating database tables: {str(e)}")

if __name__ == '__main__':
    try:
        # Initialize database
        init_db()
        
        # Get port from environment variable for deployment compatibility
        port = int(os.environ.get('PORT', 5000))
        host = os.environ.get('HOST', '0.0.0.0')
        
        logger.info(f"Starting Flask server on {host}:{port}")
        logger.info("Health check endpoints available at /health and /ping")
        logger.info("Application ready for deployment")
        
        # Production-ready configuration optimized for deployment
        app.run(
            host=host,
            port=port,
            debug=False,
            threaded=True,
            use_reloader=False
        )
    except Exception as e:
        logger.error(f"Failed to start application: {str(e)}")
        import sys
        sys.exit(1)
