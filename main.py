from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from config import Config
from forms import ContactForm
from models import db, Contact
import os

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

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
    if form.validate_on_submit():
        contact = Contact(name=form.name.data, email=form.email.data, message=form.message.data)
        db.session.add(contact)
        db.session.commit()
        flash('Your message has been sent!', 'success')
        return redirect(url_for('index'))
    return render_template('contact.html', form=form)

@app.route('/media')
def media():
    return render_template('media.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)
