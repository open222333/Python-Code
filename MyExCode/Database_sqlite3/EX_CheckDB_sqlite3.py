import sqlite3

conn = sqlite3.connect("domainName.db")
results = conn.execute("SELECT * from Domain")
allresults = results.fetchall()
for result in allresults:
    print(result)
