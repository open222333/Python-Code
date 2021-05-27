from config import DevConfig
from flask import Flask

app = Flask(__name__)
app.config.from_object(DevConfig)


@app.route('/')
def index():
    return 'Hello test'


if __name__ == '__main__':
    app.run()
