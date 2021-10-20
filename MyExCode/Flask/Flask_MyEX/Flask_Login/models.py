# models.py裡面我們要處理與資料庫相關的問題。
from __init__ import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
# __init__ 中建立的db與 login_manager 實體；
# 與密碼加密有關的werkzeug以及與login有關的flask_login。


class User(db.Model, UserMixin):
    # 繼承資料庫 db.Model UserMixin
    # tablename 資料表名稱
    __tablename__ = "users"
    # columns 欄位
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    passwordHash = db.Column(db.String(128))

    def __init__(self, email, username, password) -> None:
        """初始化"""
        self.email = email
        self.username = username
        # 實際存入的為password_hash，非password本身
        self.passwordHash = generate_password_hash(password)

    def checkPassword(self, password):
        """檢查使用者密碼"""
        return check_password_hash(self.passwordHash, password)

    @login_manager.user_loader
    # 使用login_manager裝飾器，建立loadUser函式。
    # loadUser函式的參數為userID。
    # 可以依照這個userID，對應出資料庫中實際的User。
    def loadUser(userID):
        return User.query.get(userID)
