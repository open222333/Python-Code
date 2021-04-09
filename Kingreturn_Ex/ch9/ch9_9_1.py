# pop()應用
fruits = {'西瓜': 15, '香蕉': 20, '水蜜桃': 25}
print("舊的fruits字典內容：", fruits)
objkey = '西瓜'
value = fruits.pop(objkey)
print("新的fruits字典內容：", fruits)
print("刪除內容：", objkey + ":" + str(value))
