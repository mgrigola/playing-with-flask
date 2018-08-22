from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    userName = StringField('User', validators=[DataRequired(), Length(min=3, max=20)])
    emailAddr = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    passwordConfirm = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up!')

class LoginForm(FlaskForm):
    emailAddr = StringField('Email')
    password = PasswordField('Password', validators=[DataRequired()])
    rememberCheck = BooleanField('Remember me')
    submit = SubmitField('Login')