from flask import Flask
from flask_login import LoginManager, current_user
from flask_permissions.core import Permissions
from flask_sqlalchemy import SQLAlchemy

from .config import Config


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
perms = Permissions(app, db, current_user)


from . import views
from . import database
