#from flask_login import UserMixin as UserLoginMixin
from flask_permissions.models import UserMixin as UserPermissionMixin
from werkzeug.security import generate_password_hash
from sqlalchemy import Column, Unicode, Integer
from . import db


class User(UserPermissionMixin):

    id = Column(Integer, primary_key=True)
    email = Column(Unicode(255))
    password_hash = Column(Unicode(71))

    # Identify the class to differentiate between sub-types of the UserMixin.
    __mapper_args__ = {
        'polymorphic_identity': 'user' # This can be any unique value except 'usermixin'.
    }

    __tablename__ = 'users'

    def __init__(self, email, password, roles=None):
        self.email = email
        self.set_password(password)
        UserPermissionMixin.__init__(self, roles)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)