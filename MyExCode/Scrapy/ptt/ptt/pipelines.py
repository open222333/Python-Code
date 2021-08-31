# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# Item pipelines 的典型應用：
# 清洗資料
# 驗證資料
# 過濾重複資料
# 資料存入資料庫

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


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


class MongoDBPipeline:
    '''存入mongoDB'''

    def open_spider(self, spider):
        from pymongo import MongoClient
        db_uri = spider.settings.get(
            'MONGODB_URI', 'mongodb://localhost:27017')
        db_name = spider.settings.get('MONGODB_DB_NAME', 'ptt_scrapy')
        self.db_client = MongoClient('mongodb://localhost:27017')
        self.db = self.db_client[db_name]
    pass
