import sys


class ProgressBar():
    '''進度條'''

    def __init__(self, title='Progress', symbol='=', bar_size=50) -> None:
        """

        Args:
            title (str, optional): 標題. Defaults to 'Progress'.
            symbol (str, optional): 進度條符號. Defaults to '='.
            bar_size (int, optional): 進度條大小(滿值有多少符號). Defaults to 50.
        """
        '''進度表屬性'''
        self.title = title
        self.symbol = symbol
        self.bar_size = bar_size
        # 迴圈內 使用
        self.done = 0

    def __call__(self, total: int, done=1, decimal=1, in_loop=False):
        """呼叫進度表

        Args:
            total (int): 總數
            done (int, optional): 已完成. Defaults to 1.
            decimal (int, optional): 顯示小數位. Defaults to 1.
            in_loop (bool, optional): 建立的實體是否在迴圈內使用. Defaults to False.
        """
        if in_loop:
            self.done += done
            if self.done >= total:
                self.done = total
            self.__print_progress_bar(self.done, total, decimal)
            if self.done == total:
                self.__done()
        else:
            count = 0
            while True:
                count += done
                if count >= total:
                    count = total
                self.__print_progress_bar(count, total, decimal)
                if count == total:
                    break
            self.__done()

    def __print_progress_bar(self, done: int, total: int, decimal:int):
        """繪製 進度表

        Args:
            done (int): 已完成數
            total (int): 總任務數
            decimal (int): 百分比顯示到後面幾位
        """
        # 計算百分比
        precent = float(round(100 * done / total, decimal))
        done_symbol = int(precent / 100 * self.bar_size)
        left = self.symbol * done_symbol
        right = ' ' * (self.bar_size - done_symbol)
        # 顯示進度條
        bar = f"\r{self.title}:[{left}{right}] {format(precent, f'.{decimal}f')}% {done}/{total}"
        sys.stdout.write(bar)
        sys.stdout.flush()

    def __done(self):
        print()
