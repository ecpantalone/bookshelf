from app import app, db
from app.forms import LoginForm, RegistrationForm, BookForm, EditBookForm
from app.models import User, Book
from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

#auth = Blueprint('auth', __name__)
@app.route('/')
@app.route('/index')
def index():
    return render_template(('index.html'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your registration was successful')
        return redirect(url_for('index'))
    return render_template('signup.html', title='Sign Up', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        email = User.query.filter_by(email=form.email.data).first()
        if email is None or not email.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(email, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(url_for('next_page'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('logout'))

@app.route('/profile/<username>', methods=['GET', 'POST'])
@login_required
def profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    form = BookForm()
    if form.validate_on_submit():
        book = Book(body=form.book.data, username=current_user)
        db.session.add(book)
        db.session.commit()
        flash('Your book has been added!')
        return redirect(url_for('profile'))
    books = current_user.all()
    return render_template('profile.html', title='Profile Page', user=user, books=books, form=form)

@app.route('/edit_book', methods=['GET', 'POST'])
@login_required
def edit_book():
    form = EditBookForm()
    if form.validate_on_submit():
        book.title = form.title.data
        book.author = form.author.data
        book.notes = form.notes.data
        book.purchase_date = form.purchase_date.data
        db.session.commit()
        flash('Your changes have been saved')
        return redirect(url_for('profile'))
    elif request.method == 'GET':
        form.title.data = book.title
        form.author.data = book.author
        form.notes.data = book.notes
        form.purchase_date.data = book.purchase_data
    return render_template('edit_book.html', title='Edit Book', form=form)