from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from flask_mail import Message
from werkzeug.urls import url_parse
from app import db, mail
from app.main import bp
from app.main.forms import BookForm, EditBookForm, EmptyForm, EmailBookList
from app.models import User, Book
from sqlalchemy import and_

@bp.route('/')
@bp.route('/index/')
@login_required
def index():
    return render_template(('index.html'))

@bp.route('/user/<username>', methods=['GET'])
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    current_id = current_user.id
    books = Book.query.filter_by(user_id=current_id).all()
    return render_template('user.html', title='Profile Page', user=user, books=books)

@bp.route('/add_book', methods=['GET', 'POST'])
@login_required
def add_book():
    form = BookForm()
    if form.validate_on_submit():
        book = Book(title=form.title.data, author=form.author.data, notes=form.notes.data, purchase_date=form.purchase_date.data, user_id=current_user.id)
        try:
            db.session.add(book)
            db.session.commit()
            flash('Your book has been added')
            return redirect(url_for('main.index'))
        except:
            return 'there was an issue adding that book, please try again'
    return render_template('add_book.html', title='Add Book', form=form)

@bp.route('/delete/<book_id>', methods=['POST'])
@login_required
def remove_book(book_id):
    form = EmptyForm()
    book = Book.query.get(book_id)
    if book.user_id == current_user.id:
        try:
            db.session.delete(book)
            db.session.commit()
            flash('Your book has been removed from your list.')
            return redirect(url_for('main.index'))
        except:
            return 'There was a problem deleting that book, please try again'
    return render_template('user.html', title='Profile', form=form, book=book)

@bp.route('/edit_book/<book_id>', methods=['GET', 'POST'])
@login_required
def edit_book(book_id):
    form = EditBookForm()
    book = Book.query.get(book_id)
    if request.method == 'POST' and form.validate_on_submit():
        # try:
        try:
            db.session.query(Book).filter(Book.id == book_id).update({
                "title":form.title.data, 
                "author":form.author.data, 
                "notes":form.notes.data,
                "purchase_date":form.purchase_date.data, 
                "user_id":current_user.id
            })
            db.session.commit()
            flash('Your changes have been saved')
            return redirect(url_for('main.index'))
        except:
            return 'There was an issue editing your book, please try again'
    elif request.method == 'GET':
            form.title.data = book.title 
            form.author.data = book.author 
            form.notes.data = book.notes
            form.purchase_date.data = book.purchase_date
    return render_template('edit_book.html', title='Edit Book', form=form)

@bp.route('/send_booklist/<username>', methods=['GET', 'POST'])
@login_required
def send_booklist(username):
    user = User.query.filter_by(username=username).first_or_404()
    current_id = current_user.id
    books = Book.query.filter_by(user_id=current_id).all()
    form = EmailBookList()
    if form.validate_on_submit():
        recipient = form.recipient.data
        msg = Message("A Booklist for You!", recipients=[recipient], sender='python.flask.bookshelf@gmail.com')
        msg.html = render_template('booklist.html', username=username, books=books)
        try:
            mail.send(msg)
            flash('Your booklist has been sent!')
            return redirect(url_for('main.index'))
        except:
            return 'There was an issue sending your list, please try again'
    return render_template('send_booklist.html', title='Email a Booklist', form=form, username=username, books=books)
