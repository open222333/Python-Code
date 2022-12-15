# SHA-3 的 sha3-384()

import hashlib


data = hashlib.sha384()
data.update(b'Ming-Chi Institute of Technology')  # 更新data物件內容

print('Hash Value = ', data.hexdigest())
print(type(data))
print(type(data.hexdigest()))  # 列出雜湊碼的資料型態
