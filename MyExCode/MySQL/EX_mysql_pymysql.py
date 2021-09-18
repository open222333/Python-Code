import pymysql

# 資料庫設定
db_settings = {
    "host": "172.105.39.26",
    "port": 31217,
    "user": "root",
    "password": "root",
    "db": "test_db",
    "charset": "utf8"
}

# 資料庫連線設定
# 可縮寫db = pymysql.connect("localhost","root","root","30days" )
# db = pymysql.connect(
#     host='localhost', port=3306, user='root', passwd='root', db='30days', charset='utf8')

try:
    # 建立Connection物件
    conn = pymysql.connect(**db_settings)

    # 建立Cursor物件
    with conn.cursor() as cursor:

        # 新增
        command = "INSERT INTO test_table(id, name)VALUES(%s, %s)"
        for num in range(101, 102):
            cursor.execute(command, (f"{num}", f"test{num}"))
        # 儲存變更
        conn.commit()

        command = "SELECT * FROM test_db"

except Exception as ex:
    print(ex)
