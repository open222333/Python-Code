from scrapy import cmdline
'''不輸入指令列直接執行scrapy'''

# 方法一
'''scrapy_myself_ex 須先cd到這資料夾'''
args = "scrapy crawl leetcode".split()
cmdline.execute(args)

# 方法二
if __name__ == '__main__':
    args = "scrapy crawl ptt".split()
    cmdline.execute(args)
