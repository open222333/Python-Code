from time import sleep
import sys


class ProgressBar:
    def __init__(self, tittle, symbol='=', bar_size=50) -> None:
        self.tittle = tittle
        self.symbol = symbol
        self.bar_size = bar_size

    def __call__(self, total_length, done_length=1):
        count = 0
        for i in range(total_length):
            count += done_length
            self.print_progress_bar(count, len(test_list))
            # sleep(0.1)
        self.done()

    def print_progress_bar(self, done_length, total_length):
        '''
        done_length: 目前完成的
        total_length: 總共
        '''
        show_symbol = int(self.bar_size * done_length / total_length)
        left_s = '=' * show_symbol
        right_s = ' ' * (self.bar_size - show_symbol)
        # 計算百分比
        precent = round(100 * done_length / total_length, 1)
        # 顯示進度條
        sys.stdout.write(f"\r{self.tittle}:[{left_s}{right_s}] {precent}%")
        sys.stdout.flush()

    def done(self):
        print()


class ProgressBar2():
    def __init__(self, title, symbol='=', bar_size=50) -> None:
        self.title = title
        self.symbol = symbol
        self.bar_size = bar_size

    def __call__(self, total, done=1):
        count = 0
        while True:
            count += done
            self.__print_progress_bar(count, total)
            if count == total:
                break
        print()

    def __print_progress_bar(self, done, total):
        precent = round(100 * done / total, 2)
        done_symbol = int(precent / 100 * self.bar_size)
        left = self.symbol * done_symbol
        right = ' ' * (self.bar_size - done_symbol)
        sys.stdout.write(f"\r{self.title}:[{left}{right}] {precent}% {done}/{total}")
        sys.stdout.flush()


test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test_url = 'https://www.pexels.com/zh-tw/video/3196600/download/?search_query=%E6%B8%AC%E8%A9%A6&tracking_id=01t32lpgsyg4'
ProgressBar('test').__call__(len(test_list))
