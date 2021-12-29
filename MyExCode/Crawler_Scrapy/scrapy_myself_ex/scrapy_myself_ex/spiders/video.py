import scrapy
from bs4 import BeautifulSoup
from scrapy_splash import SplashRequest
from scrapy_myself_ex.items import VideoItem
import re
import time
import requests
import traceback


class PornhubSpider(scrapy.Spider):
    name = 'pornhub'
    allowed_domains = ['www.pornhub.com']
    target_url = 'https://www.pornhub.com'

    textFilter = {
        'Newest': 'cm',
        'Hottest': 'ht',
    }
    count = 0

    def __init__(self, pages=1, wait_sec=5):
        self.pages = int(pages)
        self.wait_sec = int(wait_sec)

    def start_requests(self):
        for key in self.textFilter.keys():
            for page in range(1, self.pages + 1):
                url = f"{self.target_url}/video?o={self.textFilter[key]}&page={page}"
                yield SplashRequest(
                    url=url,
                    callback=self.first_parse,
                    args={'wait': self.wait_sec}
                )

    def first_parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        targets = soup.select('div.wrap')

        # 爬取資訊
        img_select_codes = ['data-src', 'data-thumb_url',  'data-mediumthumb']
        for tar in targets:
            self.count += 1
            data = {}
            video_select = tar.select('div.phimage a')
            views_select = tar.select('div.videoDetailsBlock span.views var')
            try:
                data['title'] = video_select[0]['title']
                img_select = video_select[0].select('img')
                for img_select_code in img_select_codes:
                    if img_select_code in img_select[0].attrs:
                        data['cover'] = img_select[0][img_select_code]
                        break
                data['views'] = views_select[0].text
                data['video_page_url'] = f"{self.target_url}{video_select[0]['href']}"

                yield SplashRequest(
                    url=data['video_page_url'],
                    callback=self.parse,
                    meta={'data': data, 'count': self.count},
                    args={'wait': self.wait_sec}
                )
            except:
                pass

    def parse(self, response):
        item = VideoItem()
        soup = BeautifulSoup(response.body, 'lxml')
        tags_select = soup.select('div.categoriesWrapper > a')

        tags = []
        for tag in tags_select:
            tags.append(tag.text)

        count = response.request.meta['count']  # 計算次數
        data = response.request.meta['data']
        data['site'] = self.target_url
        data['tags'] = tags
        item.set_item(data)

        yield item


class XvideosSpider(scrapy.Spider):
    name = 'xvideos'
    target_url = 'https://www.xvideos.com'
    allowed_domains = ['www.xvideos.com']

    def __init__(self, pages=1, wait_sec=5):
        self.pages = int(pages)
        self.wait_sec = int(wait_sec)

    def start_requests(self):
        start_urls = []

        start_urls.append(self.target_url + '/change-country/th')
        # if self.pages > 1:
        #     for num in range(1, self.pages):
        #         start_urls.append(self.target_url + f'/new/{num}')

        for url in start_urls:
            yield SplashRequest(
                url=url,
                callback=self.first_parse,
                args={'wait': self.wait_sec}
            )

    def first_parse(self, response):
        soup = BeautifulSoup(response.body, 'lxml')

        # 爬取資訊
        allvideo_perpage = soup.select_one('#content > div')
        pat = r'data-id="(.*?)"'
        data_ids = re.findall(pat, str(allvideo_perpage))
        data = {}

        for data_id in data_ids:
            try:
                thumbnum = 0
                while True:
                    cover = soup.select_one(f'#pic_{data_id}').attrs['data-src']
                    cover = cover.replace('THUMBNUM', str(thumbnum))
                    if requests.get(cover).status_code == 200:
                        break
                    thumbnum += 1
                    time.sleep(5)
                    if thumbnum == 10:
                        break

                video_info = soup.select_one(f'#video_{data_id} > div.thumb-under > p.title > a')
                href = video_info.attrs['href'].replace('THUMBNUM', str(thumbnum))

                views = soup.select_one(f'#video_{data_id} > div.thumb-under > p.metadata > span > span:nth-child(3) > span:nth-child(2)')
                try:
                    views = re.findall(r'</span> (.*?) <span class=', str(views))[0]
                except IndexError:
                    print(str(views))
                    views = 'None'
                views = str(views).strip()

                data['cover'] = cover
                data['title'] = video_info.attrs['title']
                data['views'] = views
                data['video_page_url'] = self.target_url + href
                yield SplashRequest(
                    url=data['video_page_url'],
                    callback=self.parse,
                    meta={'data': data},
                    args={'wait': self.wait_sec}
                )
            except:
                traceback.print_exc()

    def parse(self, response):
        item = VideoItem()
        soup = BeautifulSoup(response.body, 'lxml')
        data = response.request.meta['data']

        tags = []
        tags_select = soup.select('#main > div.video-metadata.video-tags-list.ordered-label-list.cropped > ul > li > a')
        for tag in tags_select:
            tags.append(tag.text)

        duration = soup.select_one('head > meta:nth-child(13)')
        duration = duration.attrs['content']

        data['site'] = self.target_url
        data['tags'] = tags
        data['duration'] = duration
        item.set_item(data)
        print(item)
        # yield item
