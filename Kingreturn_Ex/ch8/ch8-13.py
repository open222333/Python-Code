# enumerate物件應用在元組
drinks = ['coffee', 'tea', 'wine']
enumerate_drinks = enumerate(drinks)  # 數值初始是0
lst = list(enumerate_drinks)
print("轉成串列輸出，初始索引值是0 ＝ ", lst)
print(type(lst[0]))
# 使用enumerate方法產生的enumerate物件轉成串列時
# 原本的元素變成元組資料型態
