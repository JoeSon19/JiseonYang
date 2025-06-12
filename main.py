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

# Health check endpoint
@app.route('/health')
def health_check():
    try:
        # Test database connection
        with app.app_context():
            from sqlalchemy import text
            result = db.session.execute(text('SELECT 1'))
            result.fetchone()
        return {'status': 'healthy', 'database': 'connected'}, 200
    except Exception as e:
        logger.error(f"Health check failed: {str(e)}")
        return {'status': 'unhealthy', 'error': str(e)}, 500

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

if __name__ == '__main__':
    try:
        with app.app_context():
            db.create_all()
            logger.info("Database tables created successfully")
    except Exception as e:
        logger.error(f"Error creating database tables: {str(e)}")
    
    # Get port from environment variable for deployment compatibility
    port = int(os.environ.get('PORT', 5000))
    logger.info(f"Starting Flask server on 0.0.0.0:{port}")
    
    app.run(host='0.0.0.0', port=port, debug=False)
