#from flask_login import UserMixin as UserLoginMixin
import bcrypt
from flask_permissions.models import UserMixin
from . import db


connection_url = db.engine.url


class User(UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)

    def __init__(self, name, email, password, roles=None):
        """Setting params to the object."""
        import pdb; pdb.set_trace()
        self.name = name
        self.email = email.lower()
        self.password = bcrypt.hashpw(
            password.encode('utf-8'), bcrypt.gensalt())
        UserMixin.__init__(self, roles)
