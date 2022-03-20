from pymongo import MongoClient
import re

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


def get_filter_trans_jqGrid_to_pymongo(filters, *is_int: str, **multi_column: list):
    '''轉換篩選條件 js jqGrid 為 python pymongo
    is_int: 輸入欄位 欲指定型態int,
    multi_column: 多重標題 *為任何，範例：title=[viedos.ko.title, videos.zh-Hant.title]

    回傳 msg {'status': bool, 'message': 錯誤訊息(status = False 才會回傳), 'result': 轉換結果, 'rules': 搜尋的條件資料，格式為[{'filed': 欄位, 'op': 運算子, 'data': 資料}, ......]}'''
    import json
    import traceback

    def get_op(filed, data, op):
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
        if op not in op_dict.keys():
            return None
        else:
            op = op_dict[op]
            return op

    filters = json.loads(filters)

    groupOp = filters['groupOp']
    rules = filters['rules']
    msg_rules = []

    mongo_filter = {}
    msg = {}

    # 轉換 運算子
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

    # 拆解 搜尋條件
    rule_stock = []
    for rule in rules:
        filed = rule['field']
        op = rule['op']
        data = rule['data']

        # 若有欄位指定型態int
        if filed in is_int and data != "":
            data = int(data)

        # 若有多重欄位
        if filed in multi_column.keys():
            if not isinstance(multi_column[filed], list):
                filed_stack = list(multi_column[filed])
            else:
                filed_stack = multi_column[filed]
            multi = True
        else:
            multi = False

        # 轉換 true false
        if data == 'true':
            data = True
        elif data == 'false':
            data = False

        # 轉換
        trans_regex_ops = ['cn', 'nc']  # 使用正則
        if op in trans_regex_ops:
            # 轉換 regex
            data = re.compile(f'.*{data}.*')

        try:
            # 整理最後搜尋條件
            if multi:
                # 若是篩選多重欄位
                rule_temps = []
                for filed_temp in filed_stack:
                    rule_temp = get_op(filed_temp, data, op)
                    if rule_temp != None:
                        rule_temps.append(rule_temp)
                    else:
                        msg['status'] = False
                        msg['message'] = f'op: {op} 沒有設定'
                        return msg
                rule_stock.append({'$or': rule_temps})
            else:
                rule_temp = get_op(filed, data, op)
                if rule_temp != None:
                    rule_stock.append(rule_temp)
                else:
                    msg['status'] = False
                    msg['message'] = f'op: {op} 沒有設定'
                    return msg
            # 使用的規則
            msg_rules.append(
                {   
                    'filed':filed,
                    'op':op,
                    'data':data
                }
            )
        except:
            msg['status'] = False
            msg['message'] = traceback.format_exc()
            return msg

    mongo_filter[groupOp] = rule_stock
    msg['status'] = True
    msg['result'] = mongo_filter
    msg['rules'] = msg_rules
    return msg


def get_sord(request_args):
    sord = request_args['sord']
    if sord == 'asc':
        return 1
    elif sord == 'desc':
        return -1


client = MongoClient('127.0.0.1:31117')
col = client['avnight']['avdata_videos']

# 目前有的語言
languages = ['ko', 'zh-Hans', 'ja', 'zh-Hant', 'th']
titles = [f'videos.{l}.title' for l in languages]

filters = '{"groupOp":"AND","rules":[{"field":"title","op":"eq","data":"afchinatvBJ韩璐"}]}'
filter = get_filter_trans_jqGrid_to_pymongo(
    filters, 'tags', 'actors', title=titles)
print(filter)
if filter['status']:
    datas = col.find(filter['result']).sort(request_args['sidx'], get_sord(request_args))
    for data in datas:
        print(data['videos'], datas.count())
        break
else:
    print(filter)
