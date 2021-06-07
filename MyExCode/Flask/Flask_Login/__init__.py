# 這個檔案（__init__.py）的主要作用是用來初始化Python的「myproject」 packages。
# 需要匯入Flask套件，以及其他本應用程式所需要的套件。
# 例如os、flask、 flask_sqlalchemy 、flask_migrate 以及 flask_login等套件。
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, login_manager

basedir = os.path.abspath(os.path.dirname(__file__))

# app實體化
app = Flask(__name__)
app.config['SECRET_KEY'] = ''
# 與資料庫連線的參數設定
app.config['SQLALCHMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 設定db
db = SQLAlchemy(app)
Migrate(app, db)

# 建立LoginManager實體
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
