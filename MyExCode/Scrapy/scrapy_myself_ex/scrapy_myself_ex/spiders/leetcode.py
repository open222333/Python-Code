import scrapy
from scrapy_splash import SplashRequest
from bs4 import BeautifulSoup


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
        # test = response.css('#__next > div > div > div > div.col-span-4.md\:col-span-2.lg\:col-span-3 > div:nth-child(2) > div.-mx-4.md\:mx-0 > div > div > div:nth-child(2) > div:nth-child(99) > div:nth-child(2) > div > div > div > a').extract()
        # print(test)
        soup = BeautifulSoup(response)
        with open('test.html', 'w') as f:
            f.write(soup.text)
        pass
