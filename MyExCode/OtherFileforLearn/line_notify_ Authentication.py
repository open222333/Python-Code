# views.py
import re
import requests
from django.http import HttpResponse

@csrf_exempt
def notify(request):
    pattern = 'code=.*&'

    raw_uri = request.get_raw_uri()

    codes = re.findall(pattern, raw_uri)
    for code in codes:
        code = code[5:-1]
        print(code)

    # 抓取user的notify token
    user_notify_token_get_url = 'https://notify-bot.line.me/oauth/token'
    params = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': '***',  # 這邊改成自己的https://ngrok domain/notify
        'client_id': '***',  # 這邊改成自己的Notify client_id
        'client_secret': '***'  # 這邊改成自己的Notify client_secret

    }
    get_token = requests.post(user_notify_token_get_url, params=params)
    print(get_token.json())
    token = get_token.json()['access_token']
    print(token)

    # 抓取user的info
    user_info_url = 'https://notify-api.line.me/api/status'
    headers = {'Authorization': 'Bearer '+token}
    get_user_info = requests.get(user_info_url, headers=headers)
    print(get_user_info.json())
    notify_user_info = get_user_info.json()
    if notify_user_info['targetType'] == 'USER':
        User_Info.objects.filter(
            name=notify_user_info['target']).update(notify=token)
    elif notify_user_info['targetType'] == 'GROUP':
        pass
    return HttpResponse()
