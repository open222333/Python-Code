# SHA-2 的 sha256()

import hashlib

data = hashlib.sha256()
data.update(b'Ming-Chi Institute of Technology')  # 更新data物件內容

print('Hash Value = ', data.hexdigest())
print(type(data))
print(type(data.hexdigest()))  # 列出雜湊碼的資料型態
