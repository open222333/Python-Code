'''範例'''


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


def mongodb_key_word_re(host, db, collection, column, key_word):
    '''使用正則表達式 篩選出資料
    host:來源主機
    db:資料庫
    collection:集合
    column:欄位
    key_word:篩選關鍵字
    '''
    from pymongo import MongoClient
    import traceback
    import re

    try:
        client = MongoClient(host)
        pat = re.compile(r'(.*?)({})(.*?)'.format(key_word))
        col = client[db][collection]
        datas = col.find({column: pat})
    except:
        print(traceback.print_exc())
    return datas


def get_mongodb_filter(op, filed, data):
    '''篩選語法生成
    op:運算子
    filed:欄位
    data:目標資料
    '''
    # 查詢運算子範例
    op_dict = {
        'eq': {filed: {'$eq': data}},  # 等於
        'ne': {filed: {'$ne': data}},  # 不等於
        'lt': {filed: {'$lt': data}},  # 小於
        'le': {filed: {'$lte': data}},  # 小於等於
        'gt': {filed: {'$gt': data}},  # 大於
        'ge': {filed: {'$gte': data}},  # 大於等於
        'bw': {filed: {'$regex': f'^{data}'}},  # 開頭是
        'bn': {filed: {'$not': {'$regex': f'^{data}'}}},  # 開頭不是
        'in': {filed: {'$elemMatch': {'$eq': data}}},  # 在其中
        'ni': {filed: {'$not': {'$elemMatch': {'$eq': data}}}},  # 不在其中
        'ew': {filed: {'$regex': f'${data}'}},  # 結尾是
        'en': {filed: {'$not': {'$regex': f'${data}'}}},  # 結尾不是
        'cn': {filed: {'$in': [data]}},  # 內容包含(需用array)
        'nc': {filed: {'$nin': [data]}},  # 內容不包含(需用array)
    }
    try:
        return op_dict[op]
    except:
        return f'op:{op} no setting.'
