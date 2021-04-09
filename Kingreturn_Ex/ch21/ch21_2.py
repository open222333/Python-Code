import json

listObj = [{'Name': 'Peter', 'Age': 25, 'Gender': 'M'}]  # 串列資料元素是字典
jsonData = json.dumps(listObj)  # 將串列資料轉成json資料
print("將串列轉換成json的陣列", jsonData)
print("json陣列在Python的資料類型", jsonData)
