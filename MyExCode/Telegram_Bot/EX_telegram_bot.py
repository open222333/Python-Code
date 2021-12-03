from telegram.ext import Updater, dispatcher
from telegram.ext.commandhandler import CommandHandler


# 根據Token創建dispatcher與bot
token = '5020521993:AAH7drnyxRjbte5oFdlY93HXMzX5rIqAioQ'
updater = Updater(token)

# 設定調度器
dispatcher = updater.dispatcher

# 定義收到訊息後的動作
def start(bot, update):
    # 新增指令 start
    message = update.message
    chat = message['chat']
    update.message.reply_text(text='HI ' + str(chat['id']))

dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()