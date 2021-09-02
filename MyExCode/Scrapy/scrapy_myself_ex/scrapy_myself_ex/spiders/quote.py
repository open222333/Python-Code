import scrapy
from bs4 import BeautifulSoup
from scrapy_splash import SplashRequest


class QuoteSpider(scrapy.Spider):
    name = 'quote'
    # allowed_domains = ['http://quotes.toscrape.com/js/']
    start_urls = ['http://quotes.toscrape.com/js/']

    def start_requests(self):
        for url in self.start_urls:
            # args = {'wait': 5, 'proxy': 'http://139.162.125.79:8888', 'splash_headers': self.header})
            yield SplashRequest(url, self.parse, args = {'wait': 5})

    def parse(self, response):
        soup=BeautifulSoup(response.text, 'lxml')
        quotes=soup.select('div.quote span.text')
        for q in quotes:
            print(q)
            print(q.text)
        # fileName='quote_response.html'
        # with open(fileName, 'wb') as f:
        #     f.write(response.body)
        #     f.close()
