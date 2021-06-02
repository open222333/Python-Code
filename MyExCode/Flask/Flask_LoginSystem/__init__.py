import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
"""這個檔案（__init__.py）的主要作用是用來初始化Python的「myproject」 packages。首先在這個檔案裡面，我們需要匯入Flask套件，以及其他本應用程式所需要的套件。例如os、flask、 flask_sqlalchemy 、flask_migrate 以及 flask_login等套件。"""
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = ''
# 與資料庫連線的參數設定
app.config['SQLALCHMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
