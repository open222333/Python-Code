# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


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


class PronhubItem(scrapy.Item):
    cover = scrapy.Field()
    title = scrapy.Field()
    views = scrapy.Field()
    video_page_url = scrapy.Field()
