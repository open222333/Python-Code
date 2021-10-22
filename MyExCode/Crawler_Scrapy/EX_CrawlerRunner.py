"""CrawlerRunner
如果原本的程式中已經有使用 Twisted 來執行一些非同步的任務，官方建議改用 scrapy.crawler.CrawlerRunner 來啟動爬蟲，如此可以跟原本的程式使用同一個 Twisted reactor。"""

from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings

'''
get_project_settings() 方法會取得爬蟲專案中的 settings.py 檔案設定
啟動爬蟲前要提供這些設定給 Scrapy Engine
'''
runner = CrawlerRunner(get_project_settings())

d = runner.crawl('ithome')
d.addBoth(lambda _: reactor.stop())
reactor.run()
