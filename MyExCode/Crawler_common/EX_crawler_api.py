import requests
from flask import jsonify, Flask


app = Flask()


@app.route('/todaylist/p2item', methods=['GET'])
def get_todayList_p2_item(total_page=5):
    items = []
    spider_code = 'P2'
    for page in range(0, total_page):
        urls = [
            f'https://api.9bartv3.xyz/th1/home/top/videos?next={page}',
            f'https://api.9bartv3.xyz/th1/genre/1/new/videos?next={page}',
            f'https://api.9bartv3.xyz/th1/genre/5/new/videos?next={page}'
        ]
        video_type = '成人視頻'

        for url in urls:
            response = requests.get(url).json()

            if 'top' in url:
                video_item = 'HOT'
            elif 'new' in url:
                video_item = 'NEW'
            else:
                video_item = ''

            if '/home/top/videos' in url:
                video_filter = '9bar首頁 > เป็นที่นิยม TOP 100  > More'
            elif '/genre/5/new' in url:
                video_filter = '9bar首頁 > หนังโป๊ไทย  > New'
            elif '/genre/1/new' in url:
                video_filter = '9bar首頁 > หนังโป๊ญี่ปุ่น  > New'
            else:
                video_filter = ''

            for data in response['data']:
                item = {
                    'spider_code': spider_code,
                    'site_name': '9bar',
                    'video_type': video_type,
                    'video_item': video_item,
                    'video_filter': video_filter,
                    'cover': data['cover'],
                    'title': data['title'],
                    'views': data['viewers'],
                    'video_page_url': f"https://www.9bartv3.xyz/watch/{data['code']}",
                }
                items.append(item)
    return jsonify(items), 200


@app.route('/todaylist/h2item', methods=['GET'])
def get_todayList_h2_item(total_page=5):
    items = []
    spider_code = 'H2'
    for page in range(0, total_page):
        urls = [
            f'https://api.9bartv3.xyz/th1/genre/4/top/videos?next={page}',
            f'https://api.9bartv3.xyz/th1/genre/4/new/videos?next={page}',
        ]
        video_type = '成人動畫'
        for url in urls:
            response = requests.get(url).json()

            if 'top' in url:
                video_item = 'HOT'
            elif 'new' in url:
                video_item = 'NEW'
            else:
                video_item = ''

            if '/genre/4/top' in url:
                video_filter = '9bar首頁 > แอนิเมชั่น  > Ｈot'
            elif '/genre/4/new' in url:
                video_filter = '9bar首頁 > แอนิเมชั่น  > New'
            else:
                video_filter = ''

            for data in response['data']:
                item = {
                    'spider_code': spider_code,
                    'site_name': '9bar',
                    'video_type': video_type,
                    'video_item': video_item,
                    'video_filter': video_filter,
                    'cover': data['cover'],
                    'title': data['title'],
                    'views': data['viewers'],
                    'video_page_url': f"https://www.9bartv3.xyz/watch/{data['code']}",
                }
                items.append(item)
    return jsonify(items), 200
