from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class QuestionForm(FlaskForm):
    subject = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])

class AnswerForm(FlaskForm):
    content = TextAreaField('answer', validators=[DataRequired()])

class UserCreateForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('Password', validators=[
        DataRequired(), EqualTo('password2', ' The password you entered is incorrect.')])
    password2 = PasswordField('Confirm the password', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired(), Email()])

class UserLoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('Password', validators=[DataRequired()])
