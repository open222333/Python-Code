@app.route('/temp_upload_tencent')
@authenticated('page')
def temp_upload_tencent():
    tabs = {
        'ready': '未處理',
        'running': '執行中',
        'broken': '已中斷',
        'completed': '已完成',
        'all': '全部'
    }
    tab = request.args.get('tab', 'running')

    lis = ''
    for key, value in tabs.items():
        badge = ''
        active = ''
        if key == tab:
            active = 'class="active"'
        lis += ' <li id="li_'+key+'" role="presentation" '+active + \
            '><a href="javascript:go_(\'temp_upload_tencent?tab='+key+'\');void(0);">'+value + \
            '<span id="tab_temp_upload_tencent_'+key+'" class="badge">'+str(badge)+'</span></a></li>'

    return render_template('backend/temp_upload_tencent.html', tab=tab, lis=lis)


@app.route('/api_temp_upload_tencent')
@authenticated()
def api_temp_upload_tencent():
    from pymongo import MongoClient

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

    clinet = MongoClient(os.environ.get('REMOTE_AVDATA_MONGO'))
    col = clinet['avnight']['temp_upload_tencent']

    tag = request.args.get('tab', 'running')
    _search = request.args.get('_search')
    page = int(request.args.get('page', 1))
    page_row = 100
    start = page_row * (page - 1)
    end = start + page_row
    if _search == 'true':
        tag = 'all'
        msg = get_filter_trans_jqGrid_to_pymongo(dict(request.args))
        if msg['status']:
            datas = col.find(msg['result']).sort('code')
        else:
            print(msg)
    else:
        if tag == 'all':
            datas = col.find().sort('code')[start:end]
        else:
            datas = col.find({'status': tag}).sort('code')

    if datas.count() > 100:
        datas = datas[start:end]

    tut = []
    for data in datas:
        a = {
            "code": data['code'],
            "is_upload": data['is_upload'],
            "status": data['status'],
            "worker": data['worker'],
            "modified_date": data['modified_date'],
        }
        tut.append(a)

    total_page = math.ceil(datas.count() // page_row) + 1

    res = {"page": page, "total": total_page, "records": datas.count(), "rows": tut}
    return jsonify(res), 200
