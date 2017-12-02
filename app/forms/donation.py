from flask.ext.wtf import Form
from wtforms import TextField, HiddenField, DateField, SelectField
from wtforms.validators import (Required, Length, Email, ValidationError,
                                EqualTo)
from app.models import Donation


class Unique(object):

    '''
    Custom validator to check an object's attribute
    is unique. For example users should not be able
    to create an account if the account's email
    address is already in the database. This class
    supposes you are using SQLAlchemy to query the
    database.
    '''

    def __init__(self, model, field, message):
        self.model = model
        self.field = field
        self.message = message

    def __call__(self, form, field):
        check = self.model.query.filter(self.field == field.data).first()
        if check:
            raise ValidationError(self.message)


class Donate(Form):

    DROP_SITES = [('Portland (Southeast) - Adventist Medical Center','Portland (Southeast) - Adventist Medical Center'), ('Portland (North) - Legacy Emanuel Medical Center','Portland (North) - Legacy Emanuel Medical Center'), ('Portland (Southwest) - OHSU Family Medicine at Gabriel Park', 'Portland (Southwest) - OHSU Family Medicine at Gabriel Park')]

    ''' Donate milk form '''

    location = SelectField('Drop Site', validators=[Required()],
                      choices=DROP_SITES, description="test")
    date = DateField(validators=[Required()],
                      description='Date', format='%m/%d/%Y')
    amount= TextField(validators=[Required()],
                      description='Amount (oz)')
    user_email= HiddenField(validators=[Required()],
                      description='UserEmail')
