def mongodb_function(host: str, db: str, collection: str, sort_col: str):
    from pymongo import MongoClient
    import traceback
    '''地毯式 處理資料'''
    # 連線到mongodb
    client_db = MongoClient(host)
    datas = client_db[db][collection]
    min_num = 0
    max_num = 0

    count = 0

    while True:
        max_num += 100

        if max_num >= datas.count():
            max_num = datas.count()

        cursor_datas = datas.find().sort(sort_col, 1)[min_num:max_num]

        try:
            for data in cursor_datas:
                '''寫入程式碼'''
                pass
        except:
            traceback.print_exc()

        if max_num == datas.count():
            break

        min_num += 100
