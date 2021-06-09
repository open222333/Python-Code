from django.http import HttpResponse, HttpResponseBadRequest, \
    HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage
from linebot import LineBotApi, WebhookParser

# 套用settings.py 的屬性
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECERT)


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

        message_keyword = ['測試']

        for event in events:
            if isinstance(event, MessageEvent):  # 如果有訊息事件
                if event.message.text in message_keyword:
                    ans_tim(event)
                else:
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=event.message.text)
                    )
        return HttpResponse()
    else:
        return HttpResponseBadRequest()


def ans_tim(event_item):
    line_bot_api.reply_message(
        event_item.reply_token,
        TextSendMessage(text='測試回覆')
    )
