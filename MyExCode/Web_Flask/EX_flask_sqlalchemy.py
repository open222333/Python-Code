from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
sqlalchemy = SQLAlchemy(
    app, engine_options={'pool_recycle': 3600, 'pool_size': 20}
)
