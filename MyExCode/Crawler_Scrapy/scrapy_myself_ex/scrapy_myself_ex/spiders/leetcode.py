import scrapy
from scrapy_splash import SplashRequest
from bs4 import BeautifulSoup

# https://daimom3020.blogspot.com/2019/12/scrapyjson.html 研究

'''爬取leetcode'''

class LeetcodeSpider(scrapy.Spider):
    name = 'leetcode'
    # allowed_domains = ['http://quotes.toscrape.com/js/']
    # start_urls = [
    #     f'https://leetcode.com/problem-list/wpwgkgt/?page={num}' for num in range(1, 3)]
    start_urls = ['https://leetcode.com/problem-list/wpwgkgt/']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, callback=self.parse, args={'wait': 5})

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'lxml')
        # print(response.body)
        # print(soup.text)
        with open('test_b.html', 'wb') as f:
            f.write(response.body)
        with open('test.html', 'w') as f:
            f.write(soup)
