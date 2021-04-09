# 設計含有一般參數與任意數量的關鍵字參數
def build_dict(name, age, **players):  # **player可以接受任意數量關鍵字參數 將其轉化成字典
    # 建立NBA球員的字典茲酪
    info = {}  # 建立空字典
    info['Name'] = name
    info['Age'] = age
    for key, value in players.items():
        info[key] = value
    return info  # 回傳所建字典


player_dict = build_dict('James', '32', City='Cleveland', State='Ohio')
print(player_dict)
