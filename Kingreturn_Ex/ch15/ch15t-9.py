import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s : %(message)s')
logging.debug('程式開始')


def sumrange(n):
    logging.debug('計算開始')
    ans = 0
    for num in range(1, n + 1):
        ans += num
        logging.debug('num = %d ,ans = %d' % (num, ans))
    logging.debug('計算結束')
    return ans


num = 5
print('sumrange(%d) = %d' % (num, sumrange(num)))
logging.debug('程式結束')
