# 修改id = 1 的資料
import sqlite3

conn = sqlite3.connect("ch29/myInfo.db")  # 資料庫連線
sql = '''UPDATE students set name = "Tomy" where id = 1'''
results = conn.execute(sql)
conn.commit()  # 更新資料庫
results = conn.execute("SELECT name from students")
allstudents = results.fetchall()
for student in allstudents:
    print(student)
conn.close()
