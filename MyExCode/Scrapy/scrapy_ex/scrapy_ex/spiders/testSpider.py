import scrapy
import bs4
import re


class TestspiderSpider(scrapy.Spider):
    name = 'testSpider'
    allowed_domains = ['pjbar09.xyz']
    start_urls = ['https://pjbar09.xyz/']

    def parse(self, response):
        filename = "testSpider.html"
        with open(filename, 'wb') as f:
            f.write(response.body)
            f.close()
        soup = bs4.BeautifulSoup(response.text, 'lxml')
        print(response.text)
        tests = soup.find_all('li', {'class':'yellow'})
        for test in tests:
            print(test)
