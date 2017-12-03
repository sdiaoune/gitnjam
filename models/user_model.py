from wtforms import Form, StringField, validators, PasswordField
from flask_admin.contrib.pymongo import ModelView
from config.database import Mongo

mongo = Mongo()

class LoginForm(Form):
    email = StringField('Email',
                        [validators.DataRequired(),
                         validators.Length(min=6, max=50)])
    password = PasswordField('Password',
                             [validators.DataRequired(),
                              validators.Length(min=8, max=50)])

class SignupForm(Form):
    firstname = StringField('First Name', [validators.Length(min=1, max=50)])
    lastname = StringField('Last Name', [validators.Length(min=1, max=50)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password',
                             [validators.DataRequired(),
                              validators.Length(min=8, max=50),
                              validators.EqualTo('confirm_password',
                                                 message='Passwords do not match')])
    confirm_password = PasswordField('Confirm Password',
                                     [validators.DataRequired()])

class Users(Form):
    firstname = StringField('First Name', [validators.Length(min=1, max=50)])
    lastname = StringField('Last Name', [validators.Length(min=1, max=50)])
    email = StringField('Email', [validators.Length(min=6, max=50)])

class UserView(ModelView):
    column_list = ('firtname', 'lastname', 'email', 'role')
    form = Users