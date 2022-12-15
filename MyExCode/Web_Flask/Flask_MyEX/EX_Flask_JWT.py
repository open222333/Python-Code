'''
【Flask 教學系列】
淺談 JWT 與 Flask JWT 實作
https://www.maxlist.xyz/2020/05/01/flask-jwt-extended/
'''
# Part 1 – 載入 & 實例化 JWT
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask import Flask, jsonify, request

app = Flask()
jwt = JWTManager()
# 設定 JWT 密鑰
app.config['JWT_SECRET_KEY'] = 'this-should-be-change'
jwt.init_app(app)


# Part 2 – 建立 JWT Token
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if username != 'test' or password != 'test':
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)


'''
使用者登入後，前端會將 access_token 存在 cookie、localstorage、memory 或其他地方，未來呼叫後端 API 時，需要帶上 JWT，可以放在以下三種位置：

1.放在 HTTP Header 裡面
    Authorization: Bearer JWT_token
2.POST方法：放在 Request Body 裡面
    access_token=JWT_token
3.GET方法：放在 URI 裡面的一個 Query Parameter
    這邊有一個雷，預設值只允許能存取 heades 裡的 jwt token，如果要將 jwt token 放在網址參數 Query Parameter 來使用的話，需要在 config 額外設定如下：

app.config['JWT_TOKEN_LOCATION'] = ['headers','query_string']
預設值參數 query paramater 參數是 jwt，也可以在額外 config 設定 app.config['JWT_QUERY_STRING_NAME'] = jwt ：

?jwt=JWT_token
'''

# Part 3 – 後端驗證 JWT Token
# 只需要在 route 下方加上裝飾詞 @jwt_required，就會自動判斷是否有帶入正確的 JWT 了。


@app.route('/protected', methods=['GET', 'POST'])
@jwt_required
def protected():
    return jsonify(msg='ok')
