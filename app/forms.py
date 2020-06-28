from app.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, DateField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
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
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class BookForm(FlaskForm):
    title = TextAreaField('Title', validators=[DataRequired(), Length(min=1, max=200)])
    author = TextAreaField('Author', validators=[DataRequired(), Length(min=1, max=200)])
    notes = TextAreaField('Notes', validators=[DataRequired(), Length(min=1, max=500)])
    purchase_date = DateField('Date of Purchase', format='%Y-%m-%d', render_kw={"placeholder": "YYYY-MM-dd"})
    submit = SubmitField('Submit')

class EditBookForm(FlaskForm):
    title = TextAreaField('Title', validators=[DataRequired(), Length(min=1, max=200)])
    author = TextAreaField('Author', validators=[DataRequired(), Length(min=1, max=200)])
    notes = TextAreaField('Notes', validators=[DataRequired(), Length(min=1, max=500)])
    purchase_date = DateField('Date of Purchase', format='%Y-%m-%d', render_kw={"placeholder": "YYYY-MM-dd"})
    submit = SubmitField('Submit')
                
class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')

class EmailBookList(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Send Booklist')