from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(User.Mixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), index=True, unique=True)
    email = db.Column(db.String(200), index=True, unique=True)
    password_hash = db.Column(db.String(200))
    books = db.relationship('Book', backref='owner', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000), index=True, unique=False)
    author = db.Column(db.String(1000), index=True, unique=False)
    notes = db.Column(db.String(1500))
    purchase_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Book {}>'.format(self.title)

# I could see a usecase for having an Author table alongside a Book table and a join table for holding 
# all the books on a user's shelf (maybe call it Bookshelf), but ultimately I am choosing a simple db 
# approach, focusing more on function of the app itself. I would have gone the other way if I were building
# an app that was a catalog of books, where we didn't want/need duplicates.

# class Author(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(1000), index=True, unique=False)
#     last_name = db.Column(db.String(1000), index=True, uniqe=False)

#     def __repr__(self):
#         return '<Author {}>'.format(self.last_name)

# class Bookshelf(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
#     user_id = db.Column(db.Integer, db.ForeignKey('user.username'))

#     def __repr__(self):
#         return '<Bookshelf {}>'.formate(self.user_id)
