import webbrowser
import requests
import os
import time

'''開啟多個網址
讀取網址文字檔
'''


class openUrls():

    def __init__(self) -> None:
        self.url_txt = f'{os.path.dirname(__file__)}/EX_webbrowser_open_url.txt'
        # 瀏覽器位置
        # self.brower_path = '/Applications/Google Chrome.app'
        self.urls = self.__get_urls()

    def check_urls(self):
        for url in self.urls:
            # self.__open_url(url, self.brower_path)
            self.__open_url(url)
            time.sleep(1)


    def __get_urls(self):
        '''從文檔取得網址
        屬性為 url_txt '''
        with open(self.url_txt, 'r') as f:
            lines = f.readlines()
        return [line.rstrip() for line in lines]

    def __open_url(self, url):
        # try:
        #     brower_name = re.findall(r'(.*?)\.', os.path.basename(brower_path))[0]
        # except:
        #     brower_name = 'brower'
        status_code = requests.get(f'{url}').status_code
        if status_code == 200:
            webbrowser.open(f'{url}', new=1)
            # # 註冊
            # webbrowser.register(brower_name, None, webbrowser.BackgroundBrowser(brower_path))
            # # 指定 開啟網頁
            # webbrowser.get(brower_name).open(f'https://{url}', new=1)

            # open()參數new：
            # new=1: 盡可能在同一瀏覽器窗口中開啟網頁
            # new=2: 盡可能打開新的瀏覽器開啟網頁
            # new=3: 盡可能在新打開的瀏覽器，開啟新的”分頁”
        else:
            return f'{url} : {status_code}'


test = openUrls()
test.check_urls()
