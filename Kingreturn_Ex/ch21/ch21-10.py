# ch21_8.py ch21_9.py 結合
import json

fn = 'ch21/login_10.json'
try:
    with open(fn) as fnObj:
        login = json.load(fnObj)  # 依照是否能正常讀取json判斷是否為第一次登入
except Exception:
    login = input("請輸入帳號：")
    with open(fn, 'w') as fnObj:
        json.dump(login, fnObj)
        print("系統已記錄你的帳號")
else:
    print("%s 歡迎回來" % login)
# 檔案不存在為第一次登入 若檔案存在則非第一次登入
