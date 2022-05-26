# 使用遞迴的八皇后問題

class Queens:
    def __init__(self, size) -> None:
        self.queens = size * [-1]  # 預設皇后位置
        self.size = size  # 棋盤大小
        self.solve(0)  # 從row = 0 開始找
        for i in range(size):
            for j in range(size):
                if self.queens[i] == j:
                    print('Q', end='')
                else:
                    print('1', end='')
            print()

    def is_OK(self, row, col):
        '''檢查是否可以放在此 row, col位置'''
        for i in range(1, row + 1):  # 迴圈往前檢查是否衝突
            if (self.queens[row - i] == col  # 檢查欄
                or self.queens[row - i] == col - i  # 檢查左上角斜線
                    or self.queens[row - i] == col + i):  # 檢查右上角斜線
                return False  # 傳回有衝突不可使用
        return True  # 傳回可以使用

    def solve(self, row):
        '''從特定row列開始找尋皇后的位置'''
        if row == self.size:  # 終止搜尋條件
            return True
        for col in range(self.size):
            self.queens[row] = col  # 安置在 (row,col)
            if self.is_OK(row, col) and self.solve(row + 1):
                return True
        return False  # 沒有解答


Queens(8)
