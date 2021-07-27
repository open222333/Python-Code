from datetime import datetime
import sqlite3
import os

dbName = os.path.dirname(__file__) + '/data.sqlite'


def isDBExists() -> bool:
    return os.path.isfile(dbName)


def creatData():
    '''創建資料表'''
    conn = sqlite3.connect(dbName)
    cursor = conn.cursor()
    sql = 'Create table users(userid int, account text, lastLoginDate text, cumulativeDays int)'
    cursor.execute(sql)
    cursor.close()
    conn.close()


def adduser(id, name):
    conn = sqlite3.connect(dbName)
    sql = 'insert into users values(?,?,?,?)'
    conn.execute(sql, (id, name, datetime.now(), 0))
    conn.commit()
    conn.close()


def selectData(userid):
    conn = sqlite3.connect(dbName)
    searchsql = f'SELECT * from users where userid = {userid}'
    results = conn.execute(searchsql)
    for result in results:
        print(f'帳號{result[1]} 連續登入{result[3]}天')
    conn.close()


def getCol():
    '''取得資料表欄位'''
    conn = sqlite3.connect(dbName)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    col_name_list = [tuple[0] for tuple in cursor.description]
    for col_name in col_name_list:
        print(f"欄位:{col_name}")


if isDBExists() == False:
    creatData()
    adduser(1, 'test1')
    adduser(2, 'test2')
    adduser(3, 'test3')
getCol()
selectData(1)
