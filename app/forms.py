from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, PasswordField)
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):

    username = StringField("账户", validators=[DataRequired()])
    password = PasswordField("密码", validators=[DataRequired()])
    submit = SubmitField("登录")
