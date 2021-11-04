import configparser
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.http import HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.template.context_processors import csrf
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models.events import MessageEvent
from linebot.models import TextSendMessage
from .models import User, Group, Association


# 使用匯入設定加載密鑰 增加安全性
config = configparser.ConfigParser()
config.read('config.ini')
line_bot_api = LineBotApi(config.get('linebot', 'LINE_CHANNEL_ACCESS_TOKEN'))
parser = WebhookParser(config.get('linebot', 'LINE_CHANNEL_SECERT'))


commandDict = {
    "A9999": "測試用指令",
    "C0000": "查看可用指令",
    "C0001": "查詢群組ID",
    "C0002": "查詢用戶ID",
}


@csrf_exempt
def callback(request):
    if request.method == "POST":
        signature = request.headers['X-Line-Signature']
        # signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        try:
            events = parser.parse(body, signature)  # 傳入的事件
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            # setData(event)  # 第一次出現登入資料庫
            if isinstance(event, MessageEvent):  # 如果有訊息事件
                command = event.message.text
                if command in getCommand(commandDict):
                    if command == commandDict["A9999"]:
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text="此指令為開發測試用"),
                        )
                    elif command == commandDict["C0000"]:
                        text = ''
                        comlist = getCommand(commandDict)
                        for command in comlist:
                            if comlist.index(command) == len(comlist) - 1:
                                text += command
                            else:
                                text += command + "\n"
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=f"目前可用指令：\n{text}"),
                        )
                    elif command == commandDict["C0001"]:
                        getGroupID(event)
                    elif command == commandDict["C0002"]:
                        getLineID(event)
                else:
                    pass
        return HttpResponse()
    else:
        return HttpResponse()


def get_csrf(request):
    # 生成 csrf 數據，發送給前端
    x = csrf(request)
    csrf_token = x['csrf_token']
    return HttpResponse('{} ; {}'.format(str(x), csrf_token))


def getCommand(command: dict) -> list:
    """印出字典內的值"""
    commandList = [i for i in command.values()]
    return commandList


def getCommandList(*args):
    '''取得目前可用指令'''
    flag = len(args)
    commandList = ''
    for arg in args:
        commandDict = dict(arg)
        count = 1  # 換行計數
        for commandCode in commandDict:
            if count == len(commandDict):
                commandList += "%s" % (commandDict[commandCode])
            else:
                commandList += "%s\n" % (commandDict[commandCode])
                count += 1
        flag -= 1
        # 兩個指令字典間的換行
        if flag != 0:
            commandList += "\n"
        else:
            pass
    return commandList


def getGroupID(event):
    '''取得使用者的目前群組ID'''
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="此群組ID：" + event.source.group_id),
    )


def getLineID(event):
    '''取得使用者的LineID'''
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="你的用戶ID：" + event.source.user_id),
    )


def setData(event):
    userId = event.source.user_id
    groupId = event.source.group_id
    nickname = event.source.name  # 不確定
    if User().isInUserData(userId):
        pass
    else:
        User().addUserData(userId, nickname)
    if Group().isInGroupData(groupId):
        pass
    else:
        Group().addGroupData(groupId)
    if Association().isInAssociationData(userId, groupId):
        pass
    else:
        Association().addAssociationData(userId, groupId)
