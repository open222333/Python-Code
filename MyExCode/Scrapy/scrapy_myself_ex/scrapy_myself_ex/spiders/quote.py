import scrapy
from bs4 import BeautifulSoup
from scrapy_splash import SplashRequest


class QuoteSpider(scrapy.Spider):
    name = 'quote'
    # allowed_domains = ['http://quotes.toscrape.com/js/']
    start_urls = ['http://quotes.toscrape.com/js/']

    # 帶入 lua腳本 設定在args lua_source
    script = '''
    function main(splash)
        -- ...
        local element = splash:select('.element')
        local bounds = element:bounds()
        assert(element:mouse_click{x = bounds.width / 3, y = bounds.height / 3})
        -- ...
    end
    '''

    def start_requests(self):
        for url in self.start_urls:
            # args = {'wait': 5, 'proxy': 'http://139.162.125.79:8888', 'splash_headers': self.header})
            yield SplashRequest(url, self.parse, args={'wait': 5, 'lua_source': self.script})

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        quotes = soup.select('div.quote span.text')
        for q in quotes:
            print(q)
            print(q.text)
        # fileName='quote_response.html'
        # with open(fileName, 'wb') as f:
        #     f.write(response.body)
        #     f.close()
