# SHA-3 的 sha3-384()

import hashlib

data = hashlib.sha256()
data.update(b'Ming-Chi Institute of Technology')  # 更新data物件內容
print('Hash Value = ', data.hexdigest())

data2 = hashlib.sha256()
data2.update(b'ming-Chi Institute of Technology')  # 更新data物件內容
print('Hash Value = ', data2.hexdigest())
