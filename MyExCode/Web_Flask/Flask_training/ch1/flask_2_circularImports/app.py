from flask import Flask
import userdata


app = Flask(__name__)
# 避免 無限循環import的問題  Circular Imports 
userdata.init_app(app)


@app.route('/')
def index():
    return 'foo'


if __name__ == "__main__":
    app.run(debug=True)
