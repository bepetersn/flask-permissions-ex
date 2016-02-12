
from werkzeug.security import generate_password_hash
from sqlalchemy import Column, Unicode, Integer
from . import db


class User(db.Model):

    id = Column(Integer, primary_key=True)
    email = Column(Unicode(255))
    password_hash = Column(Unicode(71))

    __tablename__ = 'users'

    def __init__(self, email, password, roles=None):
        self.email = email
        self.set_password(password)
        # UserPermissionMixin.__init__(self, roles)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)