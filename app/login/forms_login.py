from config import Config

from wtforms import StringField, SubmitField, PasswordField, BooleanField
from flask_wtf import FlaskForm, RecaptchaField
from wtforms.validators import DataRequired
from flask import current_app as app



class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='Please Enter Vaild Username')])
    password = PasswordField('Password', validators = [DataRequired(message = 'Please Enter Vaild Password')])
    remember_me = BooleanField('Remember Me?')
    recaptcha = RecaptchaField()
    submit = SubmitField('Login')
