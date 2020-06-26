from flask import Flask, Blueprint
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

from app import main, auth, models

# def create_app():
#     from . import db
#     # create and configure the app
#     app = Flask(__name__)

#     app.config['SECRET_KEY']='dev'
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookshelf.db'
    
#     db.init_app(app)

#     # blueprint for auth routes in app
#     from .auth import auth as auth_blueprint
#     app.register_blueprint(auth_blueprint)

#     # blueprint for non-auth parts of app
#     from .app import app as app_blueprint
#     app.register_blueprint(app_blueprint)

#     return app