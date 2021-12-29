# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import traceback


class ScrapyMyselfExItem(scrapy.Item):
    # 範例
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class PttItem(scrapy.Item):
    # 給 pttSpider 用
    title = scrapy.Field()
    author = scrapy.Field()
    push = scrapy.Field()
    href = scrapy.Field()
    date = scrapy.Field()


class LeetcodeItem(scrapy.Item):
    title = scrapy.Field()


class VideoItem(scrapy.Item):
    site = scrapy.Field()
    cover = scrapy.Field()
    title = scrapy.Field()
    views = scrapy.Field()
    duration = scrapy.Field()
    tags = scrapy.Field()
    video_page_url = scrapy.Field()

    def set_item(self, data: dict):
        '''將dict帶入，若無設定欄位則拋出錯誤提示'''
        for key, value in data.items():
            try:
                self[key] = value
            except KeyError:
                print(f'item no "{key}" Field')
            except Exception:
                traceback.print_exc()
        return self
