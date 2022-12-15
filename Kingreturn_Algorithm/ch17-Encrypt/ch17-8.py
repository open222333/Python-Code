import hashlib


def create_password(pwd: str):
    data = hashlib.sha256()
    data.update(pwd.encode('utf-8'))
    return data.hexdigest()


acc = input('請輸入帳號:')
pwd = input('請輸入密碼:')
account = {}
account[acc] = create_password(pwd)

print('歡迎進入系統')
userid = input('請輸入帳號:')
password = input('請輸入密碼:')
if userid in account:
    if account[userid] == create_password(password):
        print('歡迎進入系統')
    else:
        print('密碼錯誤')
else:
    print('帳號錯誤')
