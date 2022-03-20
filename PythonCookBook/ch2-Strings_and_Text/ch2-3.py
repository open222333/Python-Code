'''
## 2.3 使用Shell的通配模式來比對字串

問題：

```
使用與Unix shell 底下常使用的通配模式(wildcard patterns，例如:*.py、Dat[0-9]*.csv)來比對文字。
```

解法：

```
1. fnmatch模組fnmatch()：與底層的檔案系統(取決於作業系統)相同的大小寫區分規則(case-sensitivity rules)來比對模式。
2. fnmatch模組fnmatchcase()：區分大小寫。
```

討論：

```
fnmatch的能力介於簡單的字串方法以及強大的正規運算式之間。
```
'''
from fnmatch import fnmatch, fnmatchcase
result = fnmatch('foo.txt', '*.txt')
print(result)

result = fnmatch('foo.txt', '?oo.txt')
print(result)

result = fnmatch('Dat45.csv', 'Dat[0-9]')
print(result)

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
result = [name for name in names if fnmatch(name, 'Dat*.csv')]
print(result)

# On OS X (Mac)
result = fnmatch('foo.txt', '*.TXT')  # False
# print(result)

# On Windows
results = fnmatch('foo.txt', '*.TXT')  # True

# 區分大小寫
result = fnmatchcase('foo.txt', '*.TXT')

addresses = [
    '5412 N CLARK ST',
    '5148 N CLARK',
    '5000 E 58TH',
    '2122 N CLARK ST',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON ST',
    '4801 N BROADWAY',
    '1039 W GRANVILLE AVE'
]

result = [addr for addr in addresses if fnmatch(addr, '* ST')]
print(result)

result = [addr for addr in addresses if fnmatchcase(
    addr, '54[0-9][0-9] *CLARK*')]
print(result)
