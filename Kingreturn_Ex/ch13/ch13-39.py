# most_common(n) 若省略參數n：參考鍵：值的數量由大到小傳回 n是傳回多少元素
from collections import Counter

fruits = ["apple", "orange", "apple"]
fruitsdist = Counter(fruits)
myfruts1 = fruitsdist.most_common()
print(myfruts1)
myfruts0 = fruitsdist.most_common(0)
print(myfruts0)
myfruts1 = fruitsdist.most_common(1)
print(myfruts1)
myfruts2 = fruitsdist.most_common(2)
print(myfruts2)
