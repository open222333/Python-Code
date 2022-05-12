import requests


def telegram_bot_send_message(message, chat_id, bot_token):
    '''發送訊息'''
    api_url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}'
    requests.get(api_url)


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
