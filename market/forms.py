from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, EqualTo, Length, DataRequired, ValidationError
from market.models import User


class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists, try another username')

    def validate_email_address(self,email_to_check):
        email = User.query.filter_by(email=email_to_check.data).first()
        if email:
            raise ValidationError('Email already taken!!!')

    username = StringField(label='username', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='email', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='password',
                              validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='confirm password', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='SignUp')


class LoginForm(FlaskForm):
    username = StringField(label='Username',validators=[DataRequired()])
    password = PasswordField(label='Password',validators=[DataRequired()])
    submit = SubmitField(label='SignIn')
