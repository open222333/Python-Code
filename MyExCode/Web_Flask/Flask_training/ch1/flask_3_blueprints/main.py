from flask import Flask, Blueprint
from view.api import app2

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello index"


app.register_blueprint(app2, url_prefix='/pages')
# 參數設定：url_prefix 前面網址都需要加上 pages
