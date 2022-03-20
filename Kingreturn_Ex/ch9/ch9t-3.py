fruits = {'Watermelon': 15, 'Banana': 20,
          'Pineapple': 25, 'Orange': 12, 'Apple': 18}
print('舊的字典：', fruits)
sorted_fruits = {}
# 排序後加入新字典
for fruit in sorted(fruits):
    sorted_fruits[fruit] = fruits[fruit]
print('排序後的字典：', sorted_fruits)
