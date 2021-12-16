from flask import Blueprint


app2 = Blueprint('app2', __name__)
# 可以指定新註冊的 app2 使用的 static 位置
# app2 = Blueprint('app2', __name__, static_folder='static')

# 可以指定新註冊的 app2 使用的 template 位置
# app2 = Blueprint('app2', __name__, template_folder='templates')


@app2.route('/app2')
def show():
    return "Hello Blueprint app2"
