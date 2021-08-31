import scrapy
from bs4 import BeautifulSoup
from scrapy.selector import Selector
from scrapy_splash import SplashRequest


class TestspiderSpider(scrapy.Spider):
    name = 'testSpider'
    allowed_domains = ['pjbar09.xyz']
    start_urls = ['https://pjbar09.xyz/']
    # header = {
    #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    # }
    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse, args={'wait': 5})

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        print(response)
        # tests = soup.select('ul.ul_link li.yellow')
        # for test in tests:
        #     print(test)

        # sel = Selector(response)
        # sel.css('section.section_hot_app div.area3 ul.ul_link li.yellow a')

        filename = "testSpider.html"
        with open(filename, 'wb') as f:
            f.write(response.body)
            f.close()

        # tests = soup.find_all('li', {'class':'yellow'})
        # for test in tests:
        #     print(test)
