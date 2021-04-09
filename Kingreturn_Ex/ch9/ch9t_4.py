noodles = {'牛肉麵': 100, '肉絲麵': 80, '陽春麵': 60, '大滷麵': 90, '麻醬麵': 70}
print(noodles)
new_noodles = {}
for noodle in sorted(noodles.items(), key=lambda item: item[1]):
    new_noodles[noodle[0]] = noodle[1]  # 元素是元組
print(new_noodles)
