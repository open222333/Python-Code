# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.exceptions import DropItem
from itemadapter import ItemAdapter
from pymongo import MongoClient


class ScrapyMyselfExPipeline:
    def process_item(self, item, spider):
        return item

# Item pipelines 的典型應用：
# 清洗資料
# 驗證資料
# 過濾重複資料
# 資料存入資料庫


# useful for handling different item types with a single interface


class PttPipeline:
    def process_item(self, item, spider):
        item['push'] = int(item['push'])
        return item


class DeleteNullTitlePipeline(object):
    # 去除被刪除的文章
    # 要啟用DeleteNullTitlePipeline
    # setting.py 'myFirstScrapyProject.pipelines.DeleteNullTitlePipeline': 200
    def process_item(self, item, spider):
        title = item['title']
        if title:
            return item
        else:
            raise DropItem(f'found null title {item}')


class MongoPipeline(object):
    def __init__(self, databaseIp='127.0.0.1', databasePort=27017, user="simple", password="test", mongodbName='tutorial'):
        client = MongoClient(databaseIp, databasePort)
        self.db = client[mongodbName]
        self.db.authenticate(user, password)

    def process_item(self, item, spider):
        postItem = dict(item)  # 將item轉化為字典
        self.db.scrapy.insert(postItem)  # 插入紀錄
        return item  # 在終端輸出紀錄 可不寫

    def __init__(self) -> None:
        host = settings.MONGODB_HOST
        client = MongoClient(host)
        self.data = client['test']['original']

    def process_item(self, item, spider):
        postItem = dict(item)
        self.data.scrapy.insert(postItem)
        return item


class MongoDBPipeline:
    '''存入mongoDB'''
    # https://ithelp.ithome.com.tw/articles/10207157
    # open_spider : 開始爬之前先連接MongoDB並設定參數。
    # process_item : 呼叫insert_article。
    # insert_article : 新增資料到MongoDB內。
    # close_spider : 爬取完全部後被呼叫，關閉連接。

    def open_spider(self, spider):
        # db_uri = spider.settings.get(
        #     'MONGODB_URI', 'mongodb://localhost:27017')
        # db_name = spider.settings.get('MONGODB_DB_NAME', 'ptt_scrapy')
        # self.db_client = MongoClient('mongodb://localhost:27017')
        # self.db = self.db_client[db_name]

        # host = settings.MONGODB_HOST
        self.client = MongoClient('127.0.0.1:31117')
        self.db = self.client['test']

    def process_item(self, item, spider):
        self.insert_article(item)
        return item

    def insert_article(self, item):
        item = dict(item)
        self.db.article.insert_one(item)

    def close_spider(self, spider):
        self.db_clients.close()
