import scrapy
from bs4 import BeautifulSoup
from scrapy_splash import SplashRequest
from scrapy_myself_ex.items import PronhubItem


class PornhubSpider(scrapy.Spider):
    name = 'pornhub'
    allowed_domains = ['www.pornhub.com']
    textFilter = {
        'Newest': 'cm',
        'Hottest': 'ht',
    }

    def __init__(self, pages=5, wait_sec=5):
        self.pages = int(pages)
        self.wait_sec = int(wait_sec)
        self.start_urls = []

        for filter in self.textFilter.values():
            for page in range(1, self.pages + 1):
                url = f"https://www.pornhub.com/video?o={filter}&page={page}"
                self.start_urls.append(url)

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse, args={'wait': self.wait_sec})

    def parse(self, response):
        item = PronhubItem()
        soup = BeautifulSoup(response.text, 'lxml')
        targets = soup.select('div.wrap')
        for tar in targets:
            video_select = tar.select('div.phimage a')
            img_select = video_select[0].select('img')
            views_select = tar.select('div.videoDetailsBlock span.views var')
            try:
                item['title'] = video_select[0]['title']
                img_select_codes = ['data-src', 'data-thumb_url',  'data-mediumthumb']
                img_select = video_select[0].select('img')
                for img_select_code in img_select_codes:
                    if img_select_code in img_select[0].attrs:
                        item['cover'] = img_select[0][img_select_code]
                        break
                item['views'] = views_select[0].text
                item['video_page_url'] = f"https://www.pornhub.com{video_select[0]['href']}"
            except:
                pass
            yield item
