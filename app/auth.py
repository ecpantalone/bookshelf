from flask import Blueprint, render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm, RegistrationForm
from app.models import User
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

#auth = Blueprint('auth', __name__)

@app.route('/signup')
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    form = RegistrationFor()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your registration was successful')
        return redirect(url_for('profile'))
    return render_template('signup.html', title='Sign Up', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/profile')
@login_required
def profile():
    user = {
        'username': 'Liz',
        'useremail': 'ecpantalone@gmail.com'
    }
    books = [
        {
            'title': 'The Giving Tree',
            'author': 'Shel Silverstein',
            'purchase_date': 'July 4, 2000',
            'notes': 'Great read.'
        },
        {
            'title': 'The Art of Fermentation',
            'author': 'A Fun Guy',
            'purchase_date': 'June 14, 2010',
            'notes': 'Great read.'
        }
    ]
    return render_template('profile.html', title='Profile Page', user=user, books=books)    