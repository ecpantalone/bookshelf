from flask import Blueprint, render_template
from app import app

#auth = Blueprint('auth', __name__)

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/profile')
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