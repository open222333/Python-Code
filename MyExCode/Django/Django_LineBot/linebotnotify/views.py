from django.http import HttpResponse
from django.http.response import JsonResponse
import requests
from .models import User_Info
from django.views.decorators.csrf import csrf_exempt

# 連動鏈結
# https://notify-bot.line.me/oauth/authorize?response_type=code&client_id=jz2l4k1HcnjOszeNNk4w4Z&redirect_uri=https://0adee5a7e592.ngrok.io/linebotnotify/getAuthorize&scope=notify&state=NO_STATE

ClientID = "jz2l4k1HcnjOszeNNk4w4Z"
ClientSecret = "OypnXJMWd6lUEtBmSkBifiBmg4Klqzc3NeMPixq3lbm"
RedirectUrl = "https://af0a1002f339.ngrok.io/linebotnotify/getAuthorize"


@csrf_exempt
def getLink():
    # 建立跳轉鏈結
    Url = "https://notify-bot.line.me/oauth/authorize?"
    returnUrl = Url + 'response_type=code&client_id=jz2l4k1HcnjOszeNNk4w4Z&redirect_uri=' + \
        RedirectUrl + '&scope=notify&state=NO_STATE'
    return HttpResponse(returnUrl)


def getAuthorize(request):
    # 取得 code
    if request.method == 'GET':
        code = request.GET.get('code')
    print(code)

    # 取得 access_token
    accessTokenUrl = 'https://notify-bot.line.me/oauth/token'
    accessTokenParameters = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': RedirectUrl,
        'client_id': ClientID,
        'client_secret': ClientSecret,
    }
    result = requests.post(accessTokenUrl, params=accessTokenParameters)
    accessToken = result.json()['access_token']

    # 取得user的info
    userInfoUrl = "https://notify-api.line.me/api/status"
    userInfoHeaders = {
        'Authorization': "Bearer " + accessToken,
    }
    userInfo = requests.get(userInfoUrl, headers=userInfoHeaders)
    userInfoJson = userInfo.json()
    User_Info.objects.create(
        userId=userInfoJson['target'],
        userType=userInfoJson['targetType'],
        accessToken=accessToken
    )
    return HttpResponse()


@csrf_exempt
def apiNotify(request):
    data = User_Info.objects.all().values()
    datalist = querSet_to_list(data)
    # notifyUrl = "https://notify-api.line.me/api/notify"
    # headers = {
    #     'Content-Type': 'application/x-www-form-urlencoded',
    #     'Authorization': 'Bearer ' + accessToken
    # }
    # if request.method == 'POST':
    return HttpResponse()


# 將Queryset 轉成list
def querSet_to_list(item):
    return [dict(itemlist) for itemlist in item]
