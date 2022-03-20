import sqlite3
import os


def createDB(db):
    conn = sqlite3.connect(db)
    sql = '''Create table students(
        id int,
        name text,
        gender text,
        tel text,
        score int)'''
    conn.execute(sql)
    conn.close()


def addRecord(db):
    '''新增紀錄'''
    id = int(input("id:"))
    name = input("name:")
    gender = input("gender:")
    tel = input("tel:")
    score = int(input("score:"))
    record = (id, name, gender, tel, score)
    conn = sqlite3.connect(db)
    sql = '''insert into students values(?,?,?,?,?)'''
    conn.execute(sql, record)
    conn.commit()
    conn.close()


def removeRecord(db, id):
    '''刪除紀錄'''
    sql = 'DELETE from students where id = %d' % id
    conn = sqlite3.connect(db)
    conn.execute(sql)
    conn.commit()
    conn.close()


def searchAllRecord(db):
    '''查詢所有紀錄'''
    sql = 'SELECT * from students'
    conn = sqlite3.connect(db)
    results = conn.execute(sql)
    for result in results:
        print(result)
    conn.close()


dbFile = 'ch29/data29_1.db'
# 第一次執行建立資料庫
if os.path.exists(dbFile) == False:
    createDB(dbFile)
    # 連線資料庫


print("1.增加紀錄\n2.刪除紀錄\n3.列出目前所有紀錄\n4.離開程式\n")
while True:
    flag = eval(input("請根據要使用功能輸入數字："))
    if flag == 1:
        addRecord(dbFile)
    elif flag == 2:
        sid = eval(input("請輸入要刪除的id:"))
        removeRecord(dbFile, sid)
    elif flag == 3:
        searchAllRecord(dbFile)
    elif flag == 4:
        break
    else:
        print("輸入非指定指令，請再輸入一次。")
        continue
