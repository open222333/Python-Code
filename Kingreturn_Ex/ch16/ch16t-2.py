import re

with open('ch16/ex16_2.txt') as file:
    data = file.read()
while True:
    pattern = input("請輸入要搜尋字串(多個項目使用|隔開)：")
    txts = re.findall(pattern, data)  # 搜尋結果為串列
    # 建立空字典並記錄字串出現次數
    item_dict = {}
    for txt in txts:
        if txt not in item_dict:
            item_dict[txt] = 1
        else:
            item_dict[txt] += 1
    # 遍歷字典
    for name in item_dict.keys():
        print("%s出現次數：%d" % (name, item_dict[name]))
    # 是否繼續執行搜尋
    flag = input("若繼續搜尋請輸入Y或y:")
    if flag == 'Y' or flag == 'y':
        continue
    else:
        break
