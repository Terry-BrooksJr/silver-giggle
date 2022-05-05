import datetime
import numbers
from typing_extensions import assert_type
from sqlalchemy import Integer
from wtforms import StringField, SubmitField, PasswordField, BooleanField,Flags
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
import bcrypt
from flask_login import UserMixin
from flask_rbac import RoleMixin
import json


class PlatformUser(UserMixin):
    def __init__(self, username, user_id, user_first_name, user_last_name, role, password, care_facility, date_account_created, last_date_modified, last_logged_in):
        self.username = username
        # assert isinstance(username,str)
        self.user_id = user_id
        # assert isinstance(user_id,int)
        self.user_first_name = user_first_name
        # assert isinstance(user_first_name,str)
        self.user_last_name = user_last_name
        # assert isinstance(user_last_name,str)
        self.password = password
        # assert isinstance(password, str)
        self.care_facility = care_facility
        # assert isinstance(care_facility, str)
        self.date_account_created = date_account_created
        # assert isinstance(date_account_created, datetime)
        self.last_date_modified = last_date_modified
        # assert isinstance(last_date_modified, datetime)
        self.role = role
        # assert isinstance(role. str)
        self.last_logged_in = last_logged_in
        # assert isinstance(last_logged_in, datetime)
    def __repr__(self):
        return json.dumps(self)
# * Validation Tests
        if (username, user_id, user_first_name, user_last_name, password, care_facility, date_account_created, role) == None or '':
            raise TypeError
        if not isinstance(user_first_name or user_last_name or role or username, str):
            raise ValueError("Invaild Data Type - User's Name, Role, and username must be a string")
        if not isinstance(user_id, int) and (len(username) > 8):
            raise ValueError("Invalid User ID. User ID must be all intergers not exceeding 8 characters")


    # def set_password(self, password):
    #     salt = bcrypt.gensalt()
    #     hashed_pw = bcrypt.hashpw(password, salt)


    # def verify_password(self, password):
    #     if bcrypt.checkpw(password): 
    #         return True 
    #     else:
    #         raise Exception()
    def  is_active(self):
        return super().is_active
    def is_authenticated(self):
        return super().is_authenticated
    def is_anonymous(self):
        return super().is_anonymous
    def get_id(self):
        return super().get_id
    def validate_unique_username(self,username):
        username = PlatformUser.username(username=username.data).first()
        if username:
            raise ValidationError("{} is unavailable. Please select a new username.format(request.form['username'])");

    def __repr__(self):
        return json.dumps(self, default=jsonDefault, indent=4)

        # return dict (self.username, self.user_id, self.user_first_name, self.user_last_name,self.password_hash, self.care_facility, self.date_account_created, self.role,self.last_date_modified, self.last_logged_in)222



class Role(RoleMixin):
    pass