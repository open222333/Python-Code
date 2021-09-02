import time
import scrapy
import re
from scrapy_splash import SplashRequest
from scrapy.selector import Selector


class Pz01Spider(scrapy.Spider):
    name = 'pz01'
    # allowed_domains = ['pz01.bar']
    # start_urls = ['https://pz01.bar/', 'https://pz02.bar/']
    start_urls = ['https://pz01.bar/']
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }

    datas = []

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse_first, args={'wait': 0.5, 'proxy': 'http://139.162.125.79:8888', 'splash_headers': self.header})

    def parse_first(self, response):
        query = [
            'div.bou-all div.bou-list::attr(onclick)',
            'div.bou-all div.bou-list div.bou-icon img::attr(alt)',
            'div.bou-all div.bou-list div.bou-text1::text',
            'div.bou-all div.bou-list div.bou-text2::text',
        ]
        # 取得單一元素值呼叫get()方法(Method)
        # 取得多個元素值呼叫getall()方法(Method)
        # 取得文字內容，加上「::text」關鍵字
        # 取得屬性值則加上「::attr(屬性名稱)」關鍵字
        urls = Selector(response).css(query[0]).getall()
        imgs = Selector(response).css(query[1]).getall()
        text1s = Selector(response).css(query[2]).getall()
        text2s = Selector(response).css(query[3]).getall()

        for i in range(len(query)):
            temp = {}
            temp['url'] = re.search(r"[a-zA-Z]+://[^\s']*", urls[i]).group()
            temp['img'] = imgs[i]
            temp['text1'] = text1s[i]
            temp['text2'] = text2s[i]
            self.datas.append(temp)

        for data in self.datas:
            time.sleep(1)
            yield SplashRequest(url=data['url'], callback=self.parse, args={'wait': 0.5, 'proxy': 'http://139.162.125.79:8888', 'splash_headers': self.header})

    def parse(self, response):
        title = Selector(response).css('title::text').get()
        for data in self.datas:
            if data['url'] == response.url:
                data['title'] = title
                print(data)
                break
