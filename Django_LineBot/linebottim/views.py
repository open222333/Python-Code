from django.http import HttpResponse, HttpResponseBadRequest, \
    HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage

# line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
# parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
line_bot_api = '9sNHzK9fe++M2HpTjrVMIh60iBvdkEcC+JyJy/hKbrLzOgv7Xu3qXyINBwb9tOEUzCu0NPTSoawQ73opF3fCCcTXO4MqfbJvX7qeJ725UkshR9\
    PIhXv/b7m4SKACnUytHB18BBgF4JHQY9RY4oNrBgdB04t89/1O/w1cDnyilFU='
parser = '2f3748a8f2a08838c3869627c7822d9b'


@csrf_exempt
def callback(request):
    if request.method == "POST":
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)  # 傳入的事件
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):  # 如果有訊息事件
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=event.message.text)
                )
        return HttpResponse()
    else:
        return HttpResponseBadRequest()
