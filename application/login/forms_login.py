"""
The LoginForm class creates a form for the user to login.
"""
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from flask_wtf import FlaskForm, RecaptchaField
from wtforms.validators import DataRequired



class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='Please Enter Vaild Username')])
    password = PasswordField('Password', validators = [DataRequired(message = 'Please Enter Vaild Password')])
    remember_me = BooleanField('Remember Me?')
    recaptcha = RecaptchaField()
    submit = SubmitField('Login')
