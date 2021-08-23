import scrapy


class TestspiderSpider(scrapy.Spider):
    name = 'testSpider'
    allowed_domains = ['pjbar09.xyz']
    start_urls = ['https://pjbar09.xyz/']

    def parse(self, response):
        filename = "testSpider.html"
        with open(filename, 'wb') as f:
            f.write(response.body)
