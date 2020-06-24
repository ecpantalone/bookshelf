from flask import Flask, render_template, Blueprint
from flask_sqlalchemy import SQLAlchemy

app = Blueprint('app', __name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

# @app.route('/login')
# def login():
#     return render_template('login.html')

# @app.route('/signup')
# def signup():
#     return render_template('signup.html')

# @app.route('/logout')
# def logout():
#     return render_template('logout.html')    