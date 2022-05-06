from wtforms import StringField, SubmitField, BooleanField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
import argon2
from application.models import PlatformUser


        

class CreatePlatformUser(FlaskForm):
    user_first_name = StringField("New User's First Name", validators=[InputRequired()])
    user_last_name = StringField("New User's Last Name",  validators=[InputRequired()])
    daycare_facility = StringField("Primary Daycare Location", validators=[InputRequired()])
    role = BooleanField("Check to grant the new user administrative privileges?")
    password = set
    create_user = SubmitField()
    
    # def create_username(self, user_first_name, user_last_name):
    #     username = (user_first_name[0:1] + user_last_name)
    #     while username == PlatformUser.query.filter_by(username=username).first():
    #         username = username + str((random.randint(0, 250)))
    #     return username 
        #         username =
        # try:
        #     username = (user_first_name[0:1] + user_last_name)
        #     return username
        # except: 
        #     if username == PlatformUser.query.filter_by(username=username).first():
        #         username = username + str((random.randint(0, 250)))
        #         username = 