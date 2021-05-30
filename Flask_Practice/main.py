from config import DevConfig
from flask import Flask
from flask.templating import render_template

app = Flask(__name__)
app.config.from_object(DevConfig)


@app.route('/')
def index():
    return render_template("getLink.html")


if __name__ == '__main__':
    app.run()
