# add()
cities = {'Taipei', 'Beijing', 'Tokyo'}
# 增加一般元素
cities.add('Chicago')
print('cities集合內容 ', cities)
# 增加已有元素並觀察執行結果
cities.add('Beijing')
print('cities集合內容 ', cities)
tup = (1, 2, 3)
cities.add(tup)
print('cities集合內容 ', cities)
