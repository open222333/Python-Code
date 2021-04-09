# 將程式日誌logging輸出到檔案
import logging

logging.basicConfig(filename='ch15/out15_31.txt', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s : %(message)s')
logging.debug('程式開始')


def factorial(n):
    logging.debug('factorial %s 計算開始' % n)
    ans = 1
    for i in range(1, n + 1):
        ans *= i
        logging.debug('i = ' + str(i) + ',ans = ' + str(ans))
    logging.debug('factorial %s  計算結束' % n)
    return ans


num = 5
print("factorial(%d = %d" % (num, factorial(num)))
logging.debug('程式結束')
