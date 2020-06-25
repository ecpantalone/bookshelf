from flask import Blueprint, render_template, flash, redirect
from app import app
from app.forms import LoginForm

#auth = Blueprint('auth', __name__)

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember.me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    return render_template(url_for('logout'))

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
    return render_template(url_for('profile'), title='Profile Page', user=user, books=books)    