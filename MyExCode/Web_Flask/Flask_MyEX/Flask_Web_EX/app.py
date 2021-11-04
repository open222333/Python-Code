from flask import Flask, render_template, redirect, url_for
from view.login import loginApp
import os

os.chdir(os.path.abspath(os.path.dirname(__file__)))

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'
app.register_blueprint(loginApp)


@app.route("/")
def index():
    return redirect("/login")


@app.route("/main")
def main():
    return render_template("basePage.html")


if __name__ == "__main__":
    app.run(debug=True)
