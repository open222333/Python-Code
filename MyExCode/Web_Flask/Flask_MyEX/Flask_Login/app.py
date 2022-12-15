# 建立此網站所需路由
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required
from flask import Flask
from Flask_Login import app, db
# from models import User
# from forms import LoginForm, RegistrationForm

@app.route('/')  # 首頁
def home():
    return render_template('home.html')


# @app.route('/login', methods=['GET', 'POST'])  # 登入頁
# def login():
#     # 由於需要接收form表單的資料，因此除了GET方法外，還需要POST方法。
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(email=form.email.data).first()
#         if user.checkPassword(form.password.data) and user is not None:
#             login_user(user)
#             flash("Login Success")
#             next = request.args.get('next')

#             if next == None or not next[0] == '/':
#                 next = url_for('welcome_user')
#             return redirect(next)
#     return render_template('login.html', form=form)


# @app.route('/logout')  # 登出路由
# @login_required  # 確認使用者是在登入狀態
# def logout():
#     logout_user()
#     flash('Logout')
#     return redirect(url_for('home'))


# @app.route('/register', methods=['GET', 'POST'])  # 註冊頁面
# def register():
#     form = RegistrationForm()

#     if form.validate_on_submit():
#         user = User(
#             email=form.email.data,
#             username=form.username.data,
#             password=form.password.data
#         )
#         # 增加到資料表
#         db.session.add(user)
#         db.session.commit()
#         flash("Regist Success")
#         return redirect(url_for('login'))
#     return render_template('register.html', form=form)


# @app.route("/welcome")  # 會員專區
# @login_required
# def welcome_user():
#     return render_template('welcome_user.html')


# 最後加上啟動，並且啟動debug模式。
if __name__ == '__main__':
    app.run(debug=True)
