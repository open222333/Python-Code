from scrapy import cmdline
import os
'''不輸入指令列直接執行scrapy'''


spider_name = 'leetcode'
# 設定工作資料夾
os.chdir(os.path.dirname(__file__))
# 方法一

args = f"scrapy crawl {spider_name}".split()
cmdline.execute(args)
