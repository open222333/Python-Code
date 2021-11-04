# 發短信接口
def sms_send(request):
    # http://localhost:8000/duanxin/duanxin/sms_send/?phone=18434288349
    # 1 獲取手機號
    phone = request.GET.get('電話')
    # 2生成6位驗證碼
    code = aliyunsms.get_code(6, False)
    # 3 緩存到Redis
    # cache.set(phone,code,60) #60s
    # print('判斷是否中是否有：',cache.has_key(phone))
    # print('獲取Redis驗證碼:',cache.get(phone))

    # 暫時用會話處理
    request.session['phone'] = code
    request.session.set_expiry(300)  # 設置5分鐘後過期
    print('判斷是否中是否有：', request.session.get('phone'))
    print('獲取session驗證碼:', request.session.get('phone'))
    # 4發短信
    result = aliyunsms.send_sms(phone, code)
    return HttpResponse(result)

# 短信驗證碼


def sms_check(request):
    # /duanxin/sms_check/?phone=xxx&code=xxx
    # 1.電話和手動輸入的驗證碼
    phone = request.GET.get('phone')
    code = request.GET.get('code')
    # 2.獲取redis中保存的代碼
    # print('緩存中是否包含:',cache.has_key(phone))
    # print('取值:',cache.get(phone))
    #cache_code = cache.get(phone)
    # 獲取session裡的代碼
    print('取值:', request.session.get('phone'))
    cache_code = request.session.get('phone')

    # 3. 判斷
    if code == cache_code:
        return HttpResponse(json.dumps({'result': 'OK'}))
    else:
        return HttpResponse(json.dumps({'result': 'False'}))
