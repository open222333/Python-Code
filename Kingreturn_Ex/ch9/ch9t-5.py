noodles = {'牛肉麵': 100, '肉絲麵': 80, '陽春麵': 60, '大滷麵': 90, '麻醬麵': 70}
print(noodles)
print("最貴的 = ", max(noodles.items(), key=lambda item: item[1]))
print("最便宜的 = ", min(noodles.items(), key=lambda item: item[1]))
