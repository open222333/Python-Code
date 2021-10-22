import scrapy
from scrapy import Request
'''scrapy selenium middleware 的應用方式 要看 middlewares.py'''

class ScrapySeleniumSpider(scrapy.Spider):
    name = 'scrapy_selenium'
    # allowed_domains = ['http://quotes.toscrape.com/js/']
    start_urls = ['http://quotes.toscrape.com/js/']

    def start_requests(self):
        for keyword in self.settings.get('KEYWORDS'):
            # 導出搜尋的關鍵字
            for page in range(1, self.settings.get('MAX_PAGES')):
                # 導出可爬取的頁面
                url = self.base_urls + keyword
                yield Request(url=url, meta={'page': page}, callback=self.parse, dont_filter=True)

    def parse(self, response):
        pass
