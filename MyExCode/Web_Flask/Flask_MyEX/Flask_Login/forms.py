# forms.py 處理資料輸入的相關問題。
# 匯入套件，包括flask_wtf 與 wtforms。
# 內容包括各種型態的欄位以及欄位的檢查、檢查出錯誤時的對應處理。
from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from models import User
# 在這個應用程式中需要兩個表單，
# 分別是登入用的login表單以及註冊會員時的表單，
# 至於登出的時候，不需要另外製作表單。
# 登入用的login表單命名為：LoginForm。
# 註冊用的表單命名為：RegistrationForm。
# 兩者都繼承自前面匯入的FlaskForm（源自於 flask_wtf ）


class LoginForm(FlaskForm):
    # 登入表單需要三個欄位，分別是email、password與submit（也可以不需要）
    # email使用字串格式（ StringField ）、password則使用密碼格式（ PasswordField ）
    # email格式的檢查（Email()）
    # 必填的欄位檢查（ validators=[DataRequired()] ）
    email = StringField('Email', validators[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login System')


class RegistrationForm(FlaskForm):
    # 註冊表單則需要五個欄位
    # 分別是email、username、password、pass_confirm與submit(也可以不需要)。
    # password 欄位多了一個 EqualTo( 'passConfirm', message=’密碼需要吻合’ ) 的驗證屬性。
    # 在這個欄位輸入的值需要與下面欄位的值進行比較。
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('User Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[
                             DataRequired(), EqualTo('passConfirm', message='Not match')])
    passConfirm = PasswordField('Password Verify', validators=[DataRequired()])
    submit = SubmitField('Registration')

    def checkEmail(self, filed):
        """檢查Email"""
        if User.query.filter_by(email=filed.data).first():
            raise ValidationError('Email has already been registered.')

    def checkUserName(self, field):
        """檢查UserName"""
        if User.quert.filter_by(username=field.data).first():
            raise ValidationError('User Name already exists.')
