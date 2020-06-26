from app.models import User
from datetime import date
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, DateField
from wtforms_components import DateRange
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please yse a different username.')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class BookForm(FlaskForm):
    title = TextAreaField('Title', validators=[DataRequired(), Length(min=1, max=1000)])
    author = TextAreaField('Author', validators=[DataRequired(), Length(min=1, max=1000)])
    notes = TextAreaField('Author', validators=[DataRequired(), Length(min=1, max=1500)])
    # purchase_date = DateField('Date of Purchase', validators=[date(max=date(date.today()))])
    submit = SubmitField('Submit')

class EditBookForm(FlaskForm):
    title = TextAreaField('Title', validators=[DataRequired(), Length(min=1, max=1000)])
    author = TextAreaField('Author', validators=[DataRequired(), Length(min=1, max=1000)])
    notes = TextAreaField('Author', validators=[DataRequired(), Length(min=1, max=1500)])
    # purchase_date = DateField('Date of Purchase', validators=[date(max=date(date.today()))])
    submit = SubmitField('Submit')