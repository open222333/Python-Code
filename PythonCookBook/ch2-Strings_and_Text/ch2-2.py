'''
## 2.2 在一個字串的開頭或結尾比對文字

問題：

```
需要檢查一個字串的開頭(start)或結尾(end)，以找尋特定的文字模式，例如：副檔名(filename extensions)，URL schemes...
```

解法：

```
1. 檢查字串開頭或結尾最簡單方式是startswith()、endswith()。多個選項可用元組放入參數。
2. urllib.request urlopen()函式
```

討論：

```
切片與正則表達式都可以解決這問題。
常見的資料縮減(data reductions)作業。
```

```python
if any(name for name in listdir(os.path.dirname)):
    pass
```
'''
from posix import listdir
import re
from urllib.request import urlopen
import os
filename = 'spam.txt'
result = filename.endswith('.txt')
print(result)
result = filename.startswith('file:')
print(result)

url = 'http://www.python.org'
result = url.startswith('http:')
print(result)

# os.listdir()返回指定的文件夾包含的文件或文件夾的名字的列表。
filename = os.listdir(".")
print(filename)
result = [name for name in filename if name.endswith('EX')]
print(result)
result = any(name.endswith(".py") for name in filename)
print(result)


def read_data(name: str):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()


choice = ['http:', 'https:']
url = 'http://python.org'
# result = url.startswith(choice) # TypeError: startswith first arg must be str or a tuple of str, not list
result = url.startswith(tuple(choice))
print(result)

# 切片
filename = 'spam.txt'
result = filename[-4:] == '.txt'
url = 'http://www.python.org'
print(url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp:')

# 正則表達式
result = re.match('http:|https:|ftp:', url)
print(result)

# 常見的資料縮減(data reductions)作業。
if any(name for name in listdir(os.path.dirname)):
    pass
