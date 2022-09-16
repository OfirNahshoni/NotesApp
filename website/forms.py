from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField, TextAreaField, SelectField, FileField
from wtforms.validators import Length, DataRequired, Email


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Passwords', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')

class SignupForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 100), Email()])
    full_name = StringField('Full Name', validators=[DataRequired(), Length(1, 20)])
    password1 = PasswordField('Password', validators=[DataRequired(), Length(4, 50)])
    password2 = PasswordField('Confirm Password', validators=[DataRequired(), Length(4, 50)])
    submit = SubmitField('Sign up')

class ProfileForm(FlaskForm):
    nickname = StringField('Nickname')
    phone_number = StringField('Phone Number')
    state = StringField('State')
    city = StringField('City')
    gender = SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    user_type = SelectField('User Type', choices=[('seller','Seller'), ('buyer', 'Buyer'), ('viewer', 'Viewer'), ('admin', 'Admin')])
    profession = StringField('Profession')
    addition_details = StringField('Addition Details')
    img = FileField('Upload an image')
    submit = SubmitField('Submit')
