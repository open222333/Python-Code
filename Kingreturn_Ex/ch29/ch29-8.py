import sqlite3

conn = sqlite3.connect("ch29/myInfo.db")
results = conn.execute('SELECT name, gender from students where gender = "F"')
allstudents = results.fetchall()
for recode in allstudents:
    print(recode)
conn.close()
