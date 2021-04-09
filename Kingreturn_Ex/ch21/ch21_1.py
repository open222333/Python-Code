import json

listNumbers = [5, 10, 20, 1]  # 串列資料
tupleNumbers = (1, 5, 10, 9)  # 串列資料
jsonData1 = json.dumps(listNumbers)  # 將串列資料轉成json資料
jsonData2 = json.dumps(tupleNumbers)  # 將元組資料轉成json資料
print("串列轉換成json的陣列", jsonData1)
print("元組轉換成json的陣列", jsonData2)
print("json陣列在Python的資料型態", type(jsonData1))
