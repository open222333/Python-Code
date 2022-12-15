from flask_sqlalchemy import SQLAlchemy
from flask import Flask
'''使用 sqlite 資料庫連線'''

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

db.init_app(app)


@app.route('/create_db')
def index():
    db.create_all()
    return "ok"


if __name__ == "__main__":
    app.run()
