from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, EqualTo, Length


class RegisterForm(FlaskForm):
    username = StringField(label='username', validators=Length(min=2, max=30))
    email_address = StringField(label='email', validators=Email())
    password1 = PasswordField(label='password',
                              validators=Length(min=6))
    password2 = PasswordField(label='confirm password', validators=EqualTo('password1'))
    submit = SubmitField(label='submit')
