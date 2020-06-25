from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import main
from app import auth

# db = SQLAlchemy()

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