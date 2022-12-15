# zip()打包多個物件
fields = ['Name', 'Age', 'Hometown']
info = ['Peter', '30', 'Chicago']
zipData = zip(fields, info)  # 執行zip
print(type(zipData))  # 列印zip資料型態
player = list(zipData)  # 將zip資料轉成串列
print(player)
