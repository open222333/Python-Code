# 隱藏程式日誌logging的DEBUG等級使用CRITICAL
import logging

logging.basicConfig(level=logging.CRITICAL,
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
