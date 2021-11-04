from flask import Blueprint, render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.simple import PasswordField, SubmitField


class LoginForms(FlaskForm):
    account = StringField("帳號：")
    password = PasswordField("密碼：")
    submit = SubmitField("登入")


loginApp = Blueprint('loginApp', __name__)


@loginApp.route("/login")
def index():
    form = LoginForms()
    return render_template("baseMain/login.html", form=form)
