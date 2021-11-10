import sys
import time

'''自定義 進度條'''

def progress_bar(it, prefix="", size=60, file=sys.stdout):
    '''
    it：迭代
    prefix：名稱
    size：長度
    sys.stdout 就是print的一種預設輸出格式
    sys.stdout.write() 可以不換行列印
    sys.stdout.flush() 可以立即重新整理輸出的內容
    '''
    count = len(it)

    def show(j):
        x = int(size * j / count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "=" * x, "." * (size - x), j, count))
        file.flush()
    show(0)

    for i, item in enumerate(it):
        yield item
        show(i + 1)
    file.write("\n")
    file.flush()


for i in progress_bar(range(15), "Test:", 20):
    time.sleep(1)
