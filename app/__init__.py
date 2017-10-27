from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .user import User


app = Flask(__name__, static_folder='static')
app.config.from_object("app.config")

bst = Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(userid):
    return User(userid)


from . import views, models
