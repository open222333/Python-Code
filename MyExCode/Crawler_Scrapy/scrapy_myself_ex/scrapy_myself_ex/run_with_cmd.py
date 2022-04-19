from spiders.spiders import LeetcodeSpider
import scrapy
'''不使用終端機輸入指令列執行scrapy
程式內直接執行'''


# 方法一
def run_spider_one(spider):
    # 設定工作資料夾
    import os
    from scrapy import cmdline

    os.chdir(os.path.dirname(__file__))

    args = f"scrapy crawl {spider_name}".split()
    cmdline.execute(args)


def run_spider_two(spider: scrapy.Spider):
    '''spider: scrapy.Spider 類別實例'''
    from scrapy.crawler import CrawlerProcess
    from scrapy.utils.project import get_project_settings
    import os
    os.chdir('scrapy/spiders')  # 到spider的資料夾位置
    process = CrawlerProcess(get_project_settings())
    process.crawl(spider)
    process.start()


run = int(input('輸入數字'))
if run == 1:
    # 第一種
    spider_name = 'leetcode'
    run_spider_one(spider_name)
elif run == 2:
    # 第二種
    run_spider_two(LeetcodeSpider)
else:
    print(f'數字{run} 沒設定')
