from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import BookForm, EditBookForm, EmptyForm, LoginForm, RegistrationForm
from app.models import User, Book

@app.route('/')
@app.route('/index/')
@login_required
def index():
    return render_template(('index.html'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
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
            flash('Invalid email or password')
            return redirect(url_for('login'))
        login_user(email, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/user/<username>', methods=['GET', 'POST'])
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    #books = current_user.all()
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
    return render_template('user.html', title='Profile Page', user=user, books=books)

@app.route('/add_book', methods=['GET', 'POST'])
@login_required
def add_book():
    form = BookForm()
    if form.validate_on_submit():
        book = Book(title = form.title.data, author = form.author.data, notes = form.notes.data,
        purchase_date = form.purchase_date.data)
        book.set_user_id = current_user.id
        db.session.commit()
        flash('Your book has been added')
        return redirect(url_for('index'))
    return render_template('add_book.html', title='Add Book', form=form)

@app.route('/edit_book', methods=['GET', 'POST'])
@login_required
def edit_book(book_id):
    book_id = Book.query.get(book_id)
    form = EditBookForm(book_id)
    if form.validate_on_submit():
        book.title = form.title.data
        book.author = form.author.data
        book.notes = form.notes.data
        book.purchase_date = form.purchase_date.data
        book.user_id = User.query.get(int(id))
        db.session.commit()
        flash('Your changes have been saved')
        return redirect(url_for('index'))
    return render_template('edit_book.html', title='Edit Book', form=form)

