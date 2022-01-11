import traceback
import requests
import scrapy
import time
import re

from scrapy.exceptions import CloseSpider
from scrapy_myself_ex.items import VideoItem, PttItem
from scrapy_splash import SplashRequest
from scrapy import Request

from bs4 import BeautifulSoup

# https://ithelp.ithome.com.tw/articles/10205893


class LeetcodeSpider(scrapy.Spider):
    '''爬取leetcode'''
    name = 'leetcode'
    start_urls = ['https://leetcode.com/problem-list/wpwgkgt/']
    proxy = 'http://host_ip:port'

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(
                url,
                callback=self.parse,
                meta={
                    'proxy': self.proxy  # 使用預設的proxy中間件 HttpProxyMiddleware
                },
                args={'wait': 5}
            )

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'lxml')
        pass


class ScrapySeleniumSpider(scrapy.Spider):
    '''scrapy selenium middleware 的應用方式 要看 middlewares.py'''
    name = 'scrapy_selenium'
    # allowed_domains = ['http://quotes.toscrape.com/js/']
    start_urls = ['http://quotes.toscrape.com/js/']

    def start_requests(self):
        for keyword in self.settings.get('KEYWORDS'):
            # 導出搜尋的關鍵字
            for page in range(1, self.settings.get('MAX_PAGES')):
                # 導出可爬取的頁面
                url = self.base_urls + keyword
                yield Request(url=url, meta={'page': page}, callback=self.parse, dont_filter=True)

    def parse(self, response):
        pass


class PttSpider(scrapy.Spider):
    '''爬取ptt'''
    count_page = 1
    name = 'ptt'
    allowed_domains = ['www.ptt.cc']
    start_urls = ['http://www.ptt.cc/bbs/movie/index.html']

    def parse(self, response):
        items = PttItem()
        for q in response.css('div.r-ent'):
            items['push'] = q.css('div.nrec > span.hl::text').extract_first()
            items['title'] = q.css('div.title > a::text').extract_first()
            items['href'] = q.css('div.title > a::attr(href)').extract_first()
            items['date'] = q.css('div.meta > div.date ::text').extract_first()
            items['author'] = q.css(
                'div.meta > div.author ::text').extract_first()
            yield items
        next_page_url = response.css(
            'div.action-bar > div.btn-group > a.btn::attr(href)')[3].extract()
        if (next_page_url) and (self.count_page < 10):
            self.count_page = self.count_page + 1
            new = response.urljoin(next_page_url)
        else:
            raise CloseSpider('close it')
        yield scrapy.Request(new, callback=self.parse, dont_filter=True)


class QuoteSpider(scrapy.Spider):
    '''提供爬蟲練習的網站'''
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
        num = 0
        for url in self.start_urls:
            # args = {'wait': 5, 'proxy': 'http://139.162.125.79:8888', 'splash_headers': self.header})
            num += 1
            data = {'num': num}
            yield SplashRequest(url, meta=data, cookies={'t': '1'}, callback=self.parse, args={'wait': 5, 'lua_source': self.script})

    def parse(self, response):
        print(response.request.meta)  # 印出 上一個request的meta
        soup = BeautifulSoup(response.text, 'lxml')
        quotes = soup.select('div.quote span.text')
        for q in quotes:
            print(q)
            print(q.text)

        # fileName='quote_response.html'
        # with open(fileName, 'wb') as f:
        #     f.write(response.body)
        #     f.close()


class SplashPostSpider(scrapy.Spider):
    # https://stackoverflow.com/questions/46925968/how-to-send-a-post-request-with-splashrequest-in-scrapy-splash
    '''使用SplashRequest發送post請求
    使用說明'''

    name = "splash_post"
    proxy = {
        'http': 'http://proxy.example.com:1111',
        'https': 'http://proxy.example.com:1111'
    }  # 範例 無效的鏈結

    lua_script = """
    function main(splash, args)
    assert(splash:go{
    splash.args.url,
    http_method=splash.args.http_method,
    body=splash.args.body,
    })
    assert(splash:wait(0.5))
    return {
    html = splash:html(),
    }
    end
    """

    args = {
        # lua腳本
        'lua_source': lua_script,
        'http_method': 'POST',
        # 使用proxy
        'proxy': proxy,
        # 設置最長等待時間 預設60
        'timeout': 3600,
        # 超時後中止資源加載
        'resource_timeout': 20
    }
    # has_proxy = {'wait': self.wait_sec, 'splash_headers': self.header}

    def start_requests(self):
        post_url = 'https://httpbin.org/post'
        self.args['body'] = 'foo=bar'
        yield SplashRequest(
            post_url,
            self.parse,
            endpoint='execute',
            magic_response=True,
            meta={'handle_httpstatus_all': True},
            args=self.args
        )

    def parse(self, response):
        with open('test.txt', 'a') as f:
            f.write(bytes(response.body).decode('utf-8'))


class PornhubSpider(scrapy.Spider):
    name = 'pornhub'
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


class XxxyedSpider(scrapy.Spider):
    name = 'xxxyed'
    target_url = 'https://xxxyed.com/'

    def __init__(self, pages=1, wait_sec=5):
        self.pages = int(pages)
        self.wait_sec = int(wait_sec)

    def start_requests(self):
        for page in range(1, self.pages + 1):
            url = f'{self.target_url}page/{page}/'

            yield SplashRequest(
                url=url,
                callback=self.first_parse,
                args={'wait': self.wait_sec}
            )

    def first_parse(self, response):
        soup = BeautifulSoup(response.body, 'lxml')
        data = {}
        # 爬取資訊
        videos = soup.select('#main > div.videos-list > article.loop-video > a')
        pat = r'</i>(.*?)</span>'
        for video in videos:
            cover = video.select_one('div.post-thumbnail > div > img')
            cover = cover.attrs['data-src']
            data['cover'] = cover
            data['title'] = video.attrs['title']
            try:
                views = video.select_one('span.views')
                views = re.findall(pat, str(views))[0]
            except:
                views = 'Error'
            data['views'] = views
            try:
                duration = video.select_one('span.duration')
                duration = re.findall(pat, str(duration))[0]
            except:
                duration = 'Error'
            data['duration'] = duration
            url = video.attrs['href']
            data['video_page_url'] = url

            yield SplashRequest(
                url=url,
                callback=self.parse,
                meta={'data': data},
                args={'wait': self.wait_sec}
            )

    def parse(self, response):
        item = VideoItem()
        data = response.request.meta['data']

        # 爬取tags資訊
        soup = BeautifulSoup(response.text, 'lxml')
        tags = []
        tags_select = soup.select('#video-about > div.tags > div.tags-list > a')
        for tag in tags_select:
            tag = tag.attrs['title']
            tags.append(tag)

        data['site'] = self.target_url
        data['tags'] = tags

        item.set_item(data)
