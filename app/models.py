import datetime
from sqlalchemy.ext.hybrid import hybrid_property
from flask.ext.login import UserMixin
from sqlalchemy import DateTime
import datetime

from app import db, bcrypt


class User(db.Model, UserMixin):

    ''' A user who has an account on the website. '''

    __tablename__ = 'users'

    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    phone = db.Column(db.String)
    email = db.Column(db.String, primary_key=True)
    confirmation = db.Column(db.Boolean)
    _password = db.Column(db.String)

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def _set_password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext)

    def check_password(self, plaintext):
        return bcrypt.check_password_hash(self.password, plaintext)

    def get_id(self):
        return self.email

class Donation(db.Model):

    __tablename__ = 'donations'
    id = db.Column(db.Integer, primary_key='True')
    user_email = db.Column(db.String, db.ForeignKey('users.email'))
    amount = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    location = db.Column(db.String)

    def __init__(self,user_email,amount,date,location):
        self.user_email = user_email
        self.amount = amount
        self.date = date
        self.location = location
