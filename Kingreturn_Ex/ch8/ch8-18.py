# zip()打包多個物件 恢復zip()前的串列
fields = ['Name', 'Age', 'Hometown']
info = ['Peter', '30', 'Chicago']
zipData = zip(fields, info)  # 執行zip
print(type(zipData))  # 列印zip資料型態
player = list(zipData)  # 將zip資料轉成串列
print(player)

f, i = zip(*player)  # 執行unzip
print("fields = ", f)
print("info = ", i)
