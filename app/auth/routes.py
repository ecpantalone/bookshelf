from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from flask_mail import Message
from werkzeug.urls import url_parse
from app import db, mail
from app.auth import bp
from app.auth.forms import LoginForm, RegistrationForm
from app.models import User, Book

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        try:
            db.session.add(user)
            db.session.commit()
            flash('Your registration was successful')
            return redirect(url_for('main.index'))
        except:
            return 'unsuccessful registration, try again'
    return render_template('auth/signup.html', title='Sign Up', form=form)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        try:
            email = User.query.filter_by(email=form.email.data).first()
            if email is None or not email.check_password(form.password.data):
                flash('Invalid email or password')
                return redirect(url_for('login'))
            login_user(email, remember=form.remember_me.data)
            return redirect(url_for('main.index'))
        except:
            return 'there was a problem logging in, please try again'
    return render_template('auth/login.html', title='Sign In', form=form)

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))