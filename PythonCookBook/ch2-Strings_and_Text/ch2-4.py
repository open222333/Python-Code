'''
## 2.4 比對與搜尋文字模式

問題：

```
在文字中比對(match)或搜尋特定模式(pattern)。
```

解法：

```
1. 簡單的字面值(literal)：使用字串方法，str.find()、str.endswith()、str.startswith()或類似的方法。
2. 複雜的比對工作：使用正則表達式(regular expressions)。
       - match()：匹配接近字串開頭。
       - findall()：找出所有符合。
       - finditer()：迭代的匹配。
```

討論：

```
正則表達式，使用re.compile()編譯一個模式，再使用match()、findall()、finditer()。
```
'''
import re
text = 'yeah, but no, but yeah, but no, but yeah'
# 完全比對
print(text == 'yeah')

# 在開頭或結尾比對
print(text.startswith('yeah'))
print(text.endswith('no'))

# 搜尋第一次出現位置
print(text.find('no'))

text1 = '11/27/2012'
text2 = 'Nov 27,2012'
# 簡單比對：\d+代表匹配(match)一或更多個數字(digits)
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')

datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
else:
    print('no')

if datepat.match(text2):
    print('yes')
else:
    print('no')

text = "Today is 11/27/2012. PyCon starts 3/13/2013"
print(datepat.findall('text'))

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')
print(m)

# 擷取出每組的內容
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))

for i in range(0, len(m.groups())):
    print(m.group(i))

# 找出所有匹配處(注意這裡將之分為元組)
print(datepat.findall(text))

for month, day, year in datepat.findall(text):
    print('{}-{}-{}'.format(year, month, day))

for m in datepat.finditer(text):
    print(m.groups())

m = datepat.match('11/27/2012abcdef')
print(m)
print(m.group())

datepat = re.compile(r'(\d+)/(\d+)/(\d+)$')
print(datepat.match('11/27/2012abcdef'))
print(datepat.match('11/27/2012'))

print(re.findall(r'(\d+)/(\d+)/(\d+)', text))
