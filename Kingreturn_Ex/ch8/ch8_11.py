# 串列與元組資料互換
keys = ['magic', 'xaab', 9099]  # 定義串列元素是字串與數字
tuple_keys = tuple(keys)  # 將串列改為元組
print("列印元組", keys)
print("列印串列", tuple_keys)
tuple_keys.append('secret')  # 增加元素 -- 錯誤
