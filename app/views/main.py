from flask import render_template, jsonify, redirect
from app import app
from app.forms import donation as donation_forms
from app import app, models, db
import random


@app.route('/')
@app.route('/index')
def index():
    return redirect('/user/signup')


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
    if form.validate_on_submit():
        # Create a donation
        donation = models.Donation(
            user_email=form.user_email.data,
            amount=form.amount.data,
            date=form.date,
            location=form.location.data
        )
        # Insert the donation in the database
        db.session.add(donation)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('donation/donate.html', form=form, title='Donate')
