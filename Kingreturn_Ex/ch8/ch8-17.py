fields = ['Name', 'Age', 'Hometown']
info = ['Peter', '30']
zipDate = zip(fields, info)  # 執行zip
print(type(zipDate))  # 列印zip資料型態
player = list(zipDate)  # 將zip資料轉成串列
print(player)  # 列印串列
