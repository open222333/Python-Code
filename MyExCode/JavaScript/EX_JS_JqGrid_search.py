from pymongo import MongoClient
from flask import request, jsonify
import math
import re
import os

request_args = {
    'tab': 'all',
    '_search': 'true',
    'nd': '1639641849795',
    'rows': '100',
    'page': '1',
    'sidx': 'id',
    'sord': 'asc',
    'filters': '{"groupOp":"AND","rules":[{"field":"code","op":"nc","data":"ANCHOR"}]}',
    'searchField': '',
    'searchString': '',
    'searchOper': ''
}

# $regex 與 /pattern/ 語法
# https://docs.mongodb.com/manual/reference/operator/query/regex/#regex-case-insensitive


def get_filter_trans_jqGrid_to_pymongo(request_args):
    '''轉換篩選條件 js jqGrid 為 python pymongo
    回傳 msg {'status': bool, 'message': 錯誤訊息(status = False 才會回傳), 'result': 轉換結果}'''
    import json
    filters = json.loads(request_args['filters'])

    groupOp = filters['groupOp']
    rules = filters['rules']

    mongo_filter = {}
    msg = {}

    # 轉換參考
    group_op_dict = {
        'AND': '$and',
        'OR': '$or'
    }

    # 轉換 jqGrid op為 pymongo op
    if groupOp in group_op_dict:
        groupOp = group_op_dict[groupOp]
    else:
        msg['status'] = False
        msg['message'] = f'groupOp: {groupOp} 沒有設定'
        return msg

    rule_stock = []
    for rule in rules:
        filed = rule['field']
        op = rule['op']
        datas = [data for data in str(rule['data']).split(',')]

        for i in range(len(datas)):
            if datas[i] == 'true':
                datas[i] = True
            elif datas[i] == 'false':
                datas[i] = False
            else:
                datas = [re.compile(f'.*{i}.*') for i in datas]

        op_dict = {
            'eq': {filed: datas[0]},
            'cn': {filed: {'$in': datas}},
            'nc': {filed: {'$nin': datas}}
        }
        if op in op_dict:
            op = op_dict[op]
        else:
            msg['status'] = False
            msg['message'] = f'op: {op} 沒有設定'
            return msg
        rule_stock.append(op)

    mongo_filter[groupOp] = rule_stock
    msg['status'] = True
    msg['result'] = mongo_filter
    return msg


def get_sord(request_args):
    sord = request_args['sord']
    if sord == 'asc':
        return 1
    elif sord == 'desc':
        return -1


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
    else:
        datas = col.find().sort(sidx, sord)

    # 分頁 每跳轉一頁 打一次api
    if datas.count() > page_row:
        datas = datas[start: end]

    tut = []
    ignore_key = [] #
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


# filter = get_filter_trans_jqGrid_to_pymongo(request_args)
# print(filter)
# client = MongoClient('127.0.0.1:31117')
# col = client['avnight']['temp_upload_tencent']

# datas = col.find(filter['result']).sort(request_args['sidx'], get_sord(request_args))
# print(datas.count())
# for data in datas:
#     print(data)
#     break
