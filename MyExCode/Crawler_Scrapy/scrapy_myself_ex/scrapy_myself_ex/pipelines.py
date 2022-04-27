# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.exceptions import DropItem
from itemadapter import ItemAdapter
from pymongo import MongoClient
import os
import sys
from datetime import datetime


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


class MongoPipeline_2(object):

    def __init__(self) -> None:
        from scrapy_myself_ex import settings
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
        '''當spider被打開時啟用'''
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
        # return item

    def insert_article(self, item):
        item = dict(item)
        self.db.article.insert_one(item)

    def close_spider(self, spider):
        '''當spider被關閉時啟用'''
        self.db_clients.close()


class TempleOnePipeline:
    '''mongodb 範本 insert_article 兩種'''

    def __init__(self) -> None:
        pass

    def open_spider(self, spider):
        # host = settings.MONGODB_HOST
        self.client = MongoClient('127.0.0.1:31117')
        self.db = self.client['test']

    def process_item(self, item, spider):
        self.insert_article(item)

    def insert_article(self, item):
        dir_name = __file__
        for i in range(5):
            dir_name = os.path.dirname(dir_name)

        sys.path.append(os.path.join(dir_name))
        from flask.models import Models
        item = dict(item)
        data = Models.objects(post_id=item['post_id']).first()
        if data is None:
            Models(
                post_id=item['post_id'],
                page_url=item['page_url'],
                img_url=item['img_url'],
                first_video_urls=item['first_video_urls'],
                title=item['title'],
                tags=item['tags'],
                second_video_url=item['second_video_url']
            ).save()
        else:
            # 若來源更新鏈結
            data.update(**item)
            data.save()

    # def insert_article(self, item):
    #     item = dict(item)
    #     cursor_data = self.db.testTTT.find_one({'post_id': item['post_id']})
    #     if cursor_data is None:
    #         item['created_at'] = datetime.now()
    #         item['updated_at'] = datetime.now()
    #         self.db.testTTT.insert_one(item)
    #     elif cursor_data != item:
    #         self.db.testTTT.update_one(item)

    def close_spider(self, spider):
        self.client.close()


class TempleTwoPipeline:
    '''mongodb 範本 insert_article 兩種'''

    def __init__(self) -> None:
        pass

    def open_spider(self, spider):
        from scrapy_myself_ex.settings import MONGODB_HOST
        self.client = MongoClient(MONGODB_HOST)
        self.db = self.client['test']

    def process_item(self, item, spider):
        self.insert_article(item)

    def insert_article(self, item):
        item = dict(item)
        cursor_data = self.db.testTTT.find_one({'post_id': item['post_id']})
        if cursor_data is None:
            item['created_at'] = datetime.now()
            item['updated_at'] = datetime.now()
            self.db.testTTT.insert_one(item)
        elif cursor_data != item:
            self.db.testTTT.update_one(item)

    def close_spider(self, spider):
        self.client.close()
