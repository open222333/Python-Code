from config import DevConfig
from flask import Flask, request
from flask.templating import render_template

app = Flask(__name__)
app.config.from_object(DevConfig)


@app.route('/')
@app.route('/index')
def index():
    return render_template("getLink.html")


@app.route('/<name>')
def hello(name):
    return f"Hello, {name}"


@app.route('/getname', methods=['GET'])
def getname():
    name = request.args.get('name')
    return render_template('get.html', **locals())


if __name__ == '__main__':
    app.run()
