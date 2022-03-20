from flask import Flask
from flask.helpers import url_for
from werkzeug.utils import redirect
from flask import request

app = Flask(__name__)

channelID = '1656040702'
channelSecret = '68debe05603e4431cc2ba7e424567e03'
userID = 'U34cb393ef0a5e9acb847b25765c4778d'
callbackURL = 'https://b756c1c348a9.ngrok.io'


@app.route("/")
def index():
    return redirect(url_for("getCodeLink"))


@app.route('/getCodeLink')
def getCodeLink():
    requestURL = 'https://access.line.me/oauth2/v2.1/authorize?'
    url = requestURL + 'response_type=code&client_id=' + \
        channelID + '&redirect_uri=' + callbackURL + \
        '&state=abcde&scope=profile%20openid'
    return redirect(url)


@app.route('/getCode', methods=['GET'])
def getCode():
    # 取得 code
    code = request.args.get('code')
    print(code)
    return code


@app.route("/test")
def test():
    return "Test"


if __name__ == "__main__":
    app.run(debug=True)
