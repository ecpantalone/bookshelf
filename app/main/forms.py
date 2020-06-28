from app.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, DateField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length

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
    recipient = StringField('Recipient Address', validators=[DataRequired(), Email()])
    submit = SubmitField('Send Booklist')