from types import new_class
from typing import Counter
from flask_wtf import Form
from wtforms import TextField,PasswordField,SelectField
from wtforms.fields.html5 import DateField

from wtforms.validators import DataRequired, Length,EqualTo

class loginForm(Form):
    username = TextField('username', validators=[DataRequired(), Length(min=6,max=50)])
    password = PasswordField('password', validators=[DataRequired(), Length(min=6,max=50)])

class registerForm(Form):
    username = TextField('username', validators=[DataRequired(), Length(min=6,max=50)])
    password = PasswordField('New Password', validators=[DataRequired(),
    EqualTo('confirm', message='Passwords must match'), Length(min=6,max=50)])
    confirm = PasswordField('Repeat Password')
    fname = TextField('fname', validators=[DataRequired(), Length(max=50)])
    lname = TextField('sname', validators=[DataRequired(), Length(max=50)])
    dob = DateField('dob', format='%Y-%m-%d')
    gender = SelectField('gender',choices=[('Male'),('Female'),('Other')])
class updatePass(Form):
    current = PasswordField('Repeat Password', validators=[DataRequired(), Length(min=6, max=50)])
    new = PasswordField('New Password', validators=[DataRequired(),
    EqualTo('confirm', message='Passwords must match'), Length(min=6,max=50)])
    confirm = PasswordField('Repeat Password')
