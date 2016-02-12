from flask import Flask
from flask_login import LoginManager, current_user
from flask_permissions.core import Permissions
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
db = SQLAlchemy(app)
perms = Permissions(app, db, current_user)

app.config['SECRET_KEY'] = 'FAKE'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']


from . import views
from . import database
