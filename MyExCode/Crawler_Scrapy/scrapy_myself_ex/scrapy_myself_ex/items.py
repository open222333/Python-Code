# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyMyselfExItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

# 給 pttSpider 用


class PttItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    push = scrapy.Field()
    href = scrapy.Field()
    date = scrapy.Field()


class LeetcodeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
