from django.forms import ValidationError
from wtforms import StringField, SubmitField, PasswordField, BooleanField,Flags
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from argon2 import PasswordHasher
from flask_login import UserMixin
from flask_rbac import RoleMixin

class PlatformUser(UserMixin):
    def __init__(self, username, user_id, user_first_name, user_last_name, role, password, care_facility, date_account_created, last_date_modified, last_logged_in):
        self.username = username
        self.user_id = user_id
        self.user_first_name = user_first_name
        self.user_last_name = user_last_name
        self.password = password
        self.care_facility = care_facility
        self.date_account_created = date_account_created
        self.last_date_modified = last_date_modified
        self.role = role
        self.last_logged_in = last_logged_in
# * Validation Tests
        if (username, user_id, user_first_name, user_last_name, password, care_facility, date_account_created, role) == None or '':
            raise TypeError
        if not isinstance(user_first_name or user_last_name or role or username, str):
            raise ValueError("Invaild Data Type - User's Name, Role, and username must be a string")
        if not isinstance(user_id, int) and (len(username) > 8):
            raise ValueError("Invalid User ID. User ID must be all intergers not exceeding 8 characters")
    def __repr__(self):
        return '<User {}>'.format(self.username)
    def set_password(self, password):
        hasher = PasswordHasher()
        ph = hasher.hash(password)
        self.password_hash = ph

    def verify_password(self, password):
        hasher = PasswordHasher()
        try:
            hasher.verify(self.password_hash, password)
            return True
        except Exception:
            return False
            
    def  is_active(self):
        return super().is_active()
    def is_authenticated(self):
        return super().is_authenticated
    def is_anonymous(self):
        return super().is_anonymous
    def validate_unique_username(self,username):
        username = PlatformUser.username(username=username.data).first()
        if username:
            raise ValidationError("{} is unavailable. Please select a new username.format(request.form['username'])");


class Role(RoleMixin):
    pass
