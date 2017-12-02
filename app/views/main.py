from flask import render_template, jsonify
from app import app
from app.forms import donation as donation_forms
from app import app, models, db
import random


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/map')
def map():
    return render_template('map.html', title='Map')


@app.route('/map/refresh', methods=['POST'])
def map_refresh():
    points = [(random.uniform(48.8434100, 48.8634100),
               random.uniform(2.3388000, 2.3588000))
              for _ in range(random.randint(2, 9))]
    return jsonify({'points': points})


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')

@app.route('/donate', methods=['GET','POST'])
def donate():
    form = donation_forms.Donate()
    print('hello')
    if form.validate_on_submit():
        print('hey')
        # Create a donation
        donation = models.Donation(
            user_email=form.user_email.data,
            location=form.location.data,
            date=form.date,
            amount=form.amount.data,
        )
        # Insert the donation in the database
        db.session.add(donation)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('donation/donate.html', form=form, title='Donate')
