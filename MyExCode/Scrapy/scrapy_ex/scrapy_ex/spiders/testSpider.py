from bs4 import BeautifulSoup
import scrapy
from scrapy import selector
from scrapy.http.request import Request
from scrapy.selector import Selector
from scrapy_splash import SplashRequest
from scrapy_selenium import SeleniumRequest
from scrapy.spiders import Spider

from selenium import webdriver
import os

# https://splash.readthedocs.io/en/stable/scripting-tutorial.html
# script = '''function main(splash, args)
#   splash:go("https://pjbar09.xyz/")
#   splash:wait(5)
#   local title = splash:evaljs("document.title")
#   return {title=title}
# end'''


class TestspiderSpider(scrapy.Spider):
    name = 'testSpider'
    # allowed_domains = ['pjbar09.xyz','cn.jujiarobot.com']
    start_urls = [
        'https://pjbar09.xyz/',
        # 'https://cn.jujiarobot.com',
        # 'https://g.jujiarobot.com',
    ]
    # start_urls = ['https://pz01.bar/']
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }

    # def __init__(self):
    #     self.dirpath = os.path.dirname(__file__) + '/chromedriver'
    #     self.options = webdriver.ChromeOptions()
    #     self.options.add_argument('--headless')  # 在背景執行
    #     # "/Users/4ge0/Desktop/PythonCode/MyExCode/Scrapy/scrapy_ex/chromedriver"
    #     self.browser = webdriver.Chrome(
    #         options=self.options, executable_path=self.dirpath)

    # def start_requests(self):
    #     for url in self.start_urls:
    #         return Request(url=url, callback=self.parse, headers={"User-Agent": "My UserAgent"}, meta={"proxy": "http://192.168.1.1:8050"})

    def start_requests(self):
        for url in self.start_urls:
            # 'proxy': 'http://139.162.125.79:8888',
            yield SplashRequest(url=url, callback=self.parse, args={'wait': 5, 'splash_headers': self.header})

    # def start_requests2(self):
    #     yield SplashRequest(url=url, callback=self.parse, args={'wait': 3})

    def parse(self, response):
        # # 先由self.browser進行請求
        # self.browser.get(response.url)
        # # 用scrapy選擇器獲取selenium的頁面源代碼
        # sel = Selector(text=self.browser.page_source)

        # soup = BeautifulSoup(response.text, 'lxml')
        # print(response.body)
        # tests = soup.select('ul.ul_link li.yellow')
        # for test in tests:
        #     print(test)

        sel = Selector(response)
        results = sel.css('ul.ul_link').getall()
        for result in results:
            print(result)

        # test = sel.xpath(
        #     '/html/body/span[1]/section[9]/ul/li[1]/a').extract_first()
        # test2 = sel.css('ul.ul_link li.yellow a')
        # filename = "testSpider.html"
        # with open(filename, 'a') as f:
        #     for i in test2:
        #         f.write(f"{i}\n")
        #     f.close()

        # Selector 選擇器
        # sel = Selector(response)
        # results = sel.css('div.bou-all div.bou-list div.bou-title').extract()
        # for result in results:
        #     print(result)

        filename = "testSpider.html"
        with open(filename, 'wb') as f:
            f.write(response.body)
            # for i in results:
            #     f.write(i)
            f.close()

        # tests = soup.find_all('li', {'class':'yellow'})
        # for test in tests:
        #     print(test)
