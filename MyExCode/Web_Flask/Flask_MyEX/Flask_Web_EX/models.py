from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import app

app.config['SQLALCHMY_DATABASE_URI'] = 'sqlite:///data.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app, db)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    account = db.Column(db.String(64), unique=True, index=True)
    passwordHash = db.Column(db.String(128))

    def __init__(self, account, password):
        """初始化"""
        self.account = account
        self.passwordHash = generate_password_hash(password)

    def checkPassword(self, password):
        """檢查使用者密碼"""
        return check_password_hash(self.passwordHash, password)
