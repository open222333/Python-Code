'''
1.19 同時轉換並縮減資料
問題：需要執行一個縮減函式(reduction function，例如：sum(),min(),max())，但得先轉換或過濾資料。
解法：
結合資料縮減動作和轉換動作的方式是使用產生器運算式引數(generator-expression argument)。
討論：

'''
# 計算平方和
import os
nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)

# 判斷一個目錄中是否含有任何.py檔案
# files = os.listdir('dirname')
# if any(name.endswith('.py') for name in files):
#     print('There be python!')
# else:
#     print('Sorry, no python.')

# 將一個元組輸出為CSV
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

# 跨越一個資料結構的欄位縮減資料
portfollo = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
min_shares = min(s['shares'] for s in portfollo)

s = sum((x * x for x in nums))  # 傳入 generator-expr 作為引數
s = sum(x * x for x in nums)  # 較為優雅的語法

s = sum([x * x for x in nums])  # 也可正常，但若資料量大，會創造出一個只用一次的大型暫存資料結構。

# 原本：回傳20
min_shares = min(s['shares'] for s in portfollo)
print(min_shares)

# 替代解法：回傳{'name':'', 'shares':20}
min_shares = min(portfollo, key=lambda s: s['shares'])
print(min_shares)
