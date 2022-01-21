from google.cloud import translate


# google API 翻譯 範例(要錢)
def google_translate_text(project_id, source_language_code, target_language_code, text):
    '''google API 翻譯
    https://cloud.google.com/translate/docs/supported-formats
    project_id:
    source_language_code:
    target_language_code:
    text:
    auto 用在環境變數'''
    client = translate.TranslationServiceClient()
    location = "global"
    parent = f"projects/{project_id}/locations/{location}"

    response = client.translate_text(
        request={
            "parent": parent,
            "contents": [text],
            "mime_type": "text/plain",  # mime types: text/plain, text/html
            "source_language_code": source_language_code,
            "target_language_code": target_language_code,
        }
    )

    result = []
    for translation in response.translations:
        result.append(translation.translated_text)

    return result


def has_language(language_code, datas: list) -> bool:
    '''是否有language_code'''
    stock = []
    for data in datas:
        stock.append(data['language_code'])
    return language_code in stock


def get_language_priority(source: list, *codes):
    '''語言優先度
    '''
    stock = []
    for index in range(len(codes)):
        if has_language(codes[index], source):
            stock.append(codes[index])
    return stock

def language_in_order(datas: list):
    # 語言順序 英文 日文 中文 韓文
    order = ['en', 'ja', 'zh-TW', 'ko']
    for i in range(len(order)):
        if has_language(order[i], datas):
            break
    else:
        return None
    return order[i]

def language_in_order_list(datas: list ,order) -> list:
    # 語言順序 英文 日文 中文 韓文
    order = ['en', 'ja', 'zh-TW', 'ko']
    ans = []
    for i in range(len(order)):
        if has_language(order[i], datas):
            ans.append(order[i])
    return ans


get_language_priority()

# print(google_translate_text('dgcmtcloud043', 'th', 'en', 'สวัสดี'))
