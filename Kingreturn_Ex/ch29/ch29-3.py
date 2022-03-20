# 建立一個資料庫 省略cursor物件
import sqlite3

conn = sqlite3.connect("ch29/myInfo.db")  # 資料庫連線
sql = '''Create table students(id int,name text,gender text)'''
conn.execute(sql)  # 執行SQL指令
conn.close()  # 關閉資料庫連線
