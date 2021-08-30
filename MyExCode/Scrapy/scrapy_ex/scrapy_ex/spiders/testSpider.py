import scrapy
from scrapy_splash import SplashRequest
import bs4
# import re


class TestspiderSpider(scrapy.Spider):
    name = 'testSpider'
    allowed_domains = ['pjbar09.xyz']
    start_urls = ['https://pjbar09.xyz/']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 0.5})

    def parse(self, response):
        filename = "testSpider.html"
        soup = bs4.BeautifulSoup(response.text, 'lxml')
        tests = soup.select('ul.ul_link li.yellow a')
        for test in tests:
            with open(filename, 'wb') as f:
                f.write(test.text)
                f.close()
        # tests = soup.find_all('li', {'class':'yellow'})
        # for test in tests:
        #     print(test)
