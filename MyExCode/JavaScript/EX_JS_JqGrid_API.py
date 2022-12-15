from flask import request, jsonify
from pymongo import MongoClient
from EX_JS_JqGrid_search import get_filter_trans_jqGrid_to_pymongo
import math
import os


def api_sample():
    '''JqGrid api範本 取得mongo'''
    client = MongoClient(os.environ.get('MONGO_HOST'))
    col = client['database']['collection']

    _search = request.args.get('_search')
    page = int(request.args.get('page', 1))
    sidx = request.args.get('sidx', 'code')  # 目標欄位名稱
    sord = request.args.get('sord', 'asc')  # 排序方向

    if sord == 'asc':
        sord = 1
    elif sord == 'desc':
        sord = -1

    page_row = 100
    start = page_row * (page - 1)
    end = start + page_row

    if _search == 'true':
        # 有傳遞搜尋條件
        msg = get_filter_trans_jqGrid_to_pymongo(dict(request.args))
        if msg['status']:
            datas = col.find(msg['result']).sort(sidx, sord)
        else:
            print(msg)
            datas = col.find().sort(sidx, sord)
    else:
        datas = col.find().sort(sidx, sord)

    # 分頁 每跳轉一頁 打一次api
    if datas.count() > page_row:
        datas = datas[start: end]

    tut = []
    for data in datas:
        stock = {}
        for key, value in data.items():
            stock[key] = value
        tut.append(stock)

    total_page = math.ceil(datas.count() // page_row) + 1
    res = {
        "page": page,
        "total": total_page,
        "records": datas.count(),
        "rows": tut
    }
    return jsonify, 200
