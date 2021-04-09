import sqlite3

mydata = 'ch29/myData.db'
conn = sqlite3.connect(mydata)
conn.close()