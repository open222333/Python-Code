# 將元組轉成enumerate物件再轉回元組物件
drinks = ('coffee', 'tea', 'wine')
enumerate_drinks = enumerate(drinks)  # 數值初始值是0
print("轉成元組輸出,初始值是 0 ＝ ", tuple(enumerate_drinks))
enumerate_drinks = enumerate(drinks, start=10)  # 數值初始是10
print("轉成元組輸出,初始值是 10 ＝ ", tuple(enumerate_drinks))
