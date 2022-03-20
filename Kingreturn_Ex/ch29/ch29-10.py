# 刪除id = 2
import sqlite3

conn = sqlite3.connect("ch29/myInfo.db")
sql = '''DELETE from students where id = 2'''
results = conn.execute(sql)
conn.commit()
results = conn.execute("SELECT name from students")
allstudents = results.fetchall()
for student in allstudents:
    print(student)
conn.close()
