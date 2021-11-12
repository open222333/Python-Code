from time import sleep
import sys


class ProgressBar():
    def __init__(self, title='Progress', symbol='=', bar_size=50) -> None:
        '''進度表屬性'''
        self.title = title
        self.symbol = symbol
        self.bar_size = bar_size

    def __call__(self, total: int, done=1, decimal=1):
        count = 0
        while True:
            count += done
            if count >= total:
                count = total
            self.__print_progress_bar(count, total, decimal)
            sleep(0.1)
            if count == total:
                break
        self.__done()
        
        # for i in range(total):
        #     count += done
        #     if count >= total:
        #         count = total
        #     self.__print_progress_bar(count, total, decimal)
        #     if count == total:
        #         break

    def __print_progress_bar(self, done, total, decimal):
        '''
        繪製 進度表
        done:完成數
        total:總任務數
        decimal: 百分比顯示到後面幾位
        '''
        # 計算百分比
        precent = format(float(round(100 * done / total, decimal)), f'.{decimal}f')
        done_symbol = int(precent / 100 * self.bar_size)
        left = self.symbol * done_symbol
        right = ' ' * (self.bar_size - done_symbol)
        # 顯示進度條
        sys.stdout.write(f"\r{self.title}:[{left}{right}] {precent}% {done}/{total}")
        sys.stdout.flush()

    def __done(self):
        print()


test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test_url = 'https://www.pexels.com/zh-tw/video/3196600/download/?search_query=%E6%B8%AC%E8%A9%A6&tracking_id=01t32lpgsyg4'
bar = ProgressBar2()
bar(100000, 1024)
