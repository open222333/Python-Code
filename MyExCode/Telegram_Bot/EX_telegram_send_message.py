import requests


def telegram_bot_send_message(message, chat_id, bot_token):
    '''發送訊息'''
    api_url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}'
    response = requests.get(api_url)


def telegram_bot_get_all_chat_id(bot_token, title=None):
    '''取的所有群 chat_id
    title:若有指定群名。只回傳指定群名的chat_id。'''
    api_url = f'https://api.telegram.org/bot{bot_token}/getUpdates'
    response = requests.get(api_url).json()

    stock = {}

    if response['ok']:
        for update in response['result']:
            if 'my_chat_member' in update.keys():
                update_id = update['my_chat_member']['chat']['id']
                update_title = update['my_chat_member']['chat']['title']
                update_chat_type = update['my_chat_member']['chat']['type']
                if update_chat_type == 'group':
                    stock[update_id] = update_title
    else:
        return response

    if title != None:
        for chat_id in stock.keys():
            if stock[chat_id] != title:
                del stock[chat_id]

    return stock

# response = telegram_bot_get_all_chat_id(bot_token)
# print(response)

bot_token = '5020521993:AAH7drnyxRjbte5oFdlY93HXMzX5rIqAioQ'
telegram_bot_send_message('\\', '-614834377', bot_token)
