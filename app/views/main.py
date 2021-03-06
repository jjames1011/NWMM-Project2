from flask import render_template, jsonify, redirect, request
from flask.ext.login import login_user, logout_user, login_required
from app import app
from app.forms import donation as donation_forms
from app import app, models, db
import random


@app.route('/')
@app.route('/index')
@login_required
def index():
    return redirect('/donate')


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
@login_required
#TODO: add a @login_required decorator and get the users email by accessing the current user
def donate():
    form = donation_forms.Donate()
    if request.method == 'POST':
        # Create a donation
        donation = models.Donation(
            user_email=form.user_email.data,
            amount=form.amount.data,
            date=form.date.data,
            location=form.location.data
        )
        # Insert the donation in the database
        db.session.add(donation)
        db.session.commit()
        return redirect('/user/account')

    return render_template('donation/donate.html', form=form, title='Donate')
