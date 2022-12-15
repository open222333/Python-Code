import pymysql

# 資料庫設定
db_settings = {
    "host": "172.105.39.26",
    "port": 31217,
    # "user": "root",
    "user": "user",
    "password": "password",
    "charset": "utf8"
}

# 資料庫連線設定
# 可縮寫db = pymysql.connect("localhost","root","root","30days" )
# db = pymysql.connect(
#     host='localhost', port=3306, user='root', passwd='root', db='30days', charset='utf8')
db = 'test_db'
table = 'test_table'
try:
    # 建立Connection物件
    conn = pymysql.connect(**db_settings)
    # 建立指標(游標)
    cursor = conn.cursor()
    # 建立資料庫(若存在就不建立，防止異常)
    sql = f"CREATE DATABASE IF NOT EXISTS {db}"
    cursor.execute(sql)


    db_settings['db'] = db
    conn.close()

    conn = pymysql.connect(**db_settings)
    cursor = conn.cursor()

    # 建立表
    # PRIMARY KEY
    # NOT NULL
    # AUTO_INCREMENT (一定要是 KEY)
    sql_2 = f"""CREATE TABLE IF NOT EXISTS {table}(id INT(10) , name LONGTEXT);"""
    cursor.execute(sql_2)
    conn.close()
    

    conn = pymysql.connect(**db_settings)
    # 建立Cursor物件
    with conn.cursor() as cursor:

        # 新增
        command = "INSERT INTO test_table(id, name)VALUES(%s, %s)"
        for num in range(1, 11):
            cursor.execute(command, (f"{num}", f"test{num}"))
        # 儲存變更
        conn.commit()

        command = "SELECT * FROM test_db"

except Exception as ex:
    print(ex)
