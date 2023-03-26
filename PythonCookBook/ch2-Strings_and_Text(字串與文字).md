# ch2-Strings_and_Text(字串與文字)

## 目錄

- [ch2-Strings\_and\_Text(字串與文字)](#ch2-strings_and_text字串與文字)
	- [目錄](#目錄)
- [內容](#內容)
	- [2.1 依據任意的多個定界符來切分字串](#21-依據任意的多個定界符來切分字串)
	- [2.2 在一個字串的開頭或結尾比對文字](#22-在一個字串的開頭或結尾比對文字)
	- [2.3 使用Shell的通配模式來比對字串](#23-使用shell的通配模式來比對字串)
	- [2.4 比對與搜尋文字模式](#24-比對與搜尋文字模式)
	- [2.5 搜尋並取代文字](#25-搜尋並取代文字)
	- [2.6 搜尋並取代不區分大小寫的文字](#26-搜尋並取代不區分大小寫的文字)
	- [2.7 為最短匹配指定一個正規表達式](#27-為最短匹配指定一個正規表達式)
	- [2.8 為多行的模式撰寫一個正規表達式](#28-為多行的模式撰寫一個正規表達式)
	- [2.9 以一種標準表示法正規化Unicode文字](#29-以一種標準表示法正規化unicode文字)
	- [2.10 在正規表達式中處理Unicode字元](#210-在正規表達式中處理unicode字元)
	- [2.11 剝除字串中不想要的字元](#211-剝除字串中不想要的字元)
	- [2.12 淨化與清理文字](#212-淨化與清理文字)
	- [2.13 對齊文字字串](#213-對齊文字字串)
	- [2.14 結合與串接字串](#214-結合與串接字串)
	- [2.15 在字串中插換變數](#215-在字串中插換變數)
	- [2.16 將文字重新格式化為固定數目的欄位](#216-將文字重新格式化為固定數目的欄位)
	- [2.17 在文字中處理HTML與XML的實體](#217-在文字中處理html與xml的實體)
	- [2.18 文字的單詞化(Tokenizing)](#218-文字的單詞化tokenizing)
	- [2.19 撰寫一個遞迴下降剖析器(Recursive Descent Parser)](#219-撰寫一個遞迴下降剖析器recursive-descent-parser)
	- [2.20 在位元組字串上進行文字作業](#220-在位元組字串上進行文字作業)

# 內容

## 2.1 依據任意的多個定界符來切分字串

問題：

```
需要把一個字串切分(split)成幾個欄位，但字串中界定欄位的定介符(delimiters)以及其周圍的空白數並不一致。
```

解法：

```
字串的split()可解決，若要更多彈性，則可使用re.split()。
```

討論：

```
re.split()，若正則表達式中含有用括號(parentheses)包圍的捕捉組(capture group)，匹配的文字也會出現在結果
```

範例：

```Python
import re
line = 'asdf fjdk; afed, fjek,asdf, foo'
print(re.split(r'[;,\s]\s*', line))

# 若正則表達式中含有用括號(parentheses)包圍的捕捉組(capture group)，匹配的文字也會出現在結果中。
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)

values = fields[::2]
delimiters = fields[1::2] + ['']
print(values)
print(delimiters)

# 使用相同的定界符重新格式化這個文字行
a = ''.join(v + d for v, d in zip(values, delimiters))
print(a)

b = re.split(r'(?:,|;|\s)\s*', line)
print(b)
```

範例：

```Python
```

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

範例：

```Python
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
```

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

範例：

```Python
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
```

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

範例：

```Python
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
```

## 2.5 搜尋並取代文字

問題：

```
在一個字串搜尋並取代一個文字模式
```

解法：

```
1. str.replace()：簡單的可使用此函式。
2. re模組 sub()函式：較為複雜可使用此函式。
3. calendar模組 month_abbr()函式：更複雜可使用此函式。

subn():可知道替換了多少地方。
```

討論：

```
```

範例：

```Python
import re
text = 'yeah, but no, but yeah, but no, but yeah'
result = text.replace('yeah', 'yep')
print(result)

text = 'Today is 11/27/2012. PyCon starts 3/13/2013'
result = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
print(result)

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
result = datepat.sub(r'\3-\1-\2', text)
print(result)


def change_date(m):
    from calendar import month_abbr
    '''
    引數是一個比對物件(match object)
    使用group()擷取出匹配處的特定部分。
    '''
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))


result = datepat.sub(change_date, text)
print(result)

newtext, n = datepat.subn(r'\3-\1-\2', text)
print(newtext)
print(n)
```

## 2.6 搜尋並取代不區分大小寫的文字

問題：

```
以不區分大小寫(case-insensitive)的方式搜尋並取代文字。
```

解法：

```
re.IGNORECASE(flag)，不區分大小寫的比對。
```

討論：

```
```

範例：

```Python
import re

text = 'UPPER PYTHON, lower python, Mixed Python'
result = re.findall('python', text, re.IGNORECASE)
print(result)


def matchcase(word: str):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.upper()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace


result = re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)
print(result)
```

## 2.7 為最短匹配指定一個正規表達式

問題：

```
使用一個正規表達式(regular expressions)比對一個文字模式(text pattern)，但所識別出來的是符合一個模式的最長匹配，需改成最短匹配。
```

解法：

```
.*加上？ 就會進行最短匹配。
```

討論：

```
```

範例：

```Python
import re
str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
text2 = 'Computer says "no." Phone says "yes."'
result = re.findall(str_pat, text1)
print(result)

str_pat_2 = re.compile(r'\"(.*?)\"')
result = str_pat_2.findall(text2)
print(result)
```

## 2.8 為多行的模式撰寫一個正規表達式

問題：

```
試著使用一個正規表達式(reqular expression)來比對一個區塊(block)，希望比對動作能夠跨越數行。
```

解法：

```
正規表達式的. 不匹配換行字元(newline)。(?:.|\n)指定一個非捕捉組。
```

討論：

```
re.compile() 接受一個旗標 re.DOTALL，用處：匹配所有字元，包含(newline)
```

範例：

```Python
import re

comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a
multiline comment */'''
result = comment.findall(text1)
print(result)
# 多行無法比對
result = comment.findall(text2)
print(result)

comment = re.compile(r'/\*((?:.|\n)*?)\*/')
result = comment.findall(text2)
print(result)

# 旗標 re.DOTALL，用處：匹配所有字元，包含(newline)
comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
result = comment.findall(text2)
print(result)
```

## 2.9 以一種標準表示法正規化Unicode文字

問題：

```
正在處理Unicode字串，得確定所有的字串都使用相同的底層表示法。
```

解法：

```
使用unicodedata模組normalize()函式 將文字正規化。
NFC代表字元應該是組成完整的。
NFD代表字元應該是透過結合字元的使用而完全分解開來。
也支援NFKC NFKD形式的正規化。
```

討論：

```
combining()函式測試一個字元是否為一個結合字元。
```

範例：

```Python
import unicodedata
s1 = "Spicy Jalape\u00f1o"
s2 = "Spicy Jalapen\u0303o"
print(s1)
print(s2)
print(s1 == s2)
print(len(s1))
print(len(s2))

t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(t1 == t2)
print(ascii(t1))

t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)
print(t3 == t4)
print(ascii(t3))

s = '\ufb01'
print(s)

# 注意 前面結合起來的字元在此被拆開了
print(unicodedata.normalize('NFKD', s))
print(unicodedata.normalize('NFKC', s))
```

## 2.10 在正規表達式中處理Unicode字元

問題：

```
使用正規表達式處理文字，但對Unicode有疑慮。
```

解法：

```
re模組，已納入某些Unicode字元類別的基礎知識。
執行比對與搜尋動作時，先把所有的文字正規化或淨化(sanitize)為一種標準行事。(參閱訣竅2.9)
```

討論：

```
若將Unicode與正規表達式混合一起使用，可使用第三方regex程式庫(http://pypi.python.org/pypi/regex)。
```

範例：

```Python
import re

num = re.compile('\d+')
# ASCII數字
print(num.match('123'))
# 阿拉伯數字
print(num.match('\u0661\u0662\u0663'))

# 以下regex能匹配幾個不同的阿拉伯code pages(代碼頁)中的所有字元
arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')
pat = re.compile('stra\u00dfe', re.IGNORECASE)
s = 'straβe'
print(pat.match(s))
pat.match(s.upper())  # 不匹配
print(s.upper())
```

## 2.11 剝除字串中不想要的字元

問題：

```
想要剝除(strip)不想要的字元。
```

解法：

```
strip() lstrip() rstrip()
```

討論：

```
處理內部的空白，需使用replace()或正規表達式(reqular expression)
運算式lines = (line.strip() for line in f)，有效率的原因，不會先把資料讀到任何暫存器，只會建立一個迭代器(iterator)，而這個迭代器產出的每個文字行都會套用剝除動作。
```

範例：

```Python
# 剔除空白
s = '    hello world \n'
result = s.strip()
print(result)

result = s.lstrip()
print(result)

result = s.rstrip()
print(result)

# 剝除給定字元
t = '-----hello====='
result = t.lstrip('-')
print(result)

result = t.rstrip('=')
print(result)
```

## 2.12 淨化與清理文字


問題：

```
清理奇怪的文字 例如: pythoй
```

解法：

```
str.upper() str.lower() 將文字轉換成標準模式
str.replace() re.sub() 替換特定字元
unicodedata.normalize() 正規化文字 如訣竅2.9
```

討論：

```
類似的訣竅可套用到位元組(byte)
```

範例：

```Python
s = 'python is awesome\n'
# 建立轉譯表
remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None  # 刪除
}

a = s.translate(remap)
print(a)
cmd_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
b = unicodedata.normalize('NFD', a)
b.translate(cmd_chrs)

digitmap = {
    c: ord('0') + unicodedata.digit(chr(c)) for c in range(sys.maxunicode) if unicodedata.category(chr(c) == 'Nd')
}

print(len(digitmap))

# 阿拉伯數字字元(Arabic digits)
x = '\u0661\u0662\u0663'
x.translate(digitmap)

# 對文字進行基本清理工作
b.encode('ascii', 'ignore').decode('ascii')
```

## 2.13 對齊文字字串

問題：

```
格式化文字 套用某種對齊(alignment)
```

解法：

```
text = 'Hello World'
print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))

使用format()函式 可用在字串也可用在其他值
```

討論：

```
舊的程式碼使用%來進行格式化 新的應優先使用format()
```

範例：

```Python
text = 'Hello World'

# 使用基本對齊
print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))

print(text.rjust(20, '='))
print(text.center(20, '*'))

print(format(text, '>20'))
print(format(text, '<20'))
print(format(text, '^20'))

print(format(text, '=>20s'))
print(format(text, '*^20s'))

# 格式化多個值
print('{:>10s} {:>10s}'.format('Hello', 'World'))

x = 1.2345
print(format(x, '>10'))
print(format(x, '^10.2f'))
```

## 2.14 結合與串接字串

問題：

```
將許多小字串結合在一起成為一個大字串
```

解法：

```
使用join()
```

討論：

```
使用+運算子來連接大量字串是很沒效率的，因為必須進行多次記憶體複製以及垃圾回收。

# 若字串都很小 以下可能提供較好的效能
f.write(chunk1 + chunk2)

# 若字串都很大 以下可能提供較好的效能 因避免 建立大型暫存結果並複製大區塊記憶體
f.write(chunk1)
f.write(chunk2)
```

範例：

```Python
# 使用join()
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print(' '.join(parts))
print(','.join(parts))
print(''.join(parts))

# 結合少數字串可用+
a = 'Is Chicago'
b = 'Not Chicago?'
print(a + ' ' + b)

# 使用format()
print('{} {}'.format(a, b))

# 結合字串字面值 直接並列在一起
c = 'Hello' 'World'
print(c)

# 使用一個產生器運算式(generator expression)同時把資料轉為字串並串接起來。
data = ['ACME', 50, 91.1]
print(','.join(str(d) for d in data))

# 若在撰寫的程式碼需要大量小型字串建置輸出
# 產生器函式不需知道細節，只需產出(yield)各個部分

def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'


def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
    yield ''.join(parts)


with open('test.txt', 'w') as f:
    for part in combine(sample(), 32768):
        f.write(part)

# 沒有效率的寫法
s = ''
for p in parts:
	s += p
```

## 2.15 在字串中插換變數

問題：

```
```

解法：

```
```

討論：

```
```

範例：

```Python
```

## 2.16 將文字重新格式化為固定數目的欄位

問題：

```
```

解法：

```
```

討論：

```
```

範例：

```Python
```

## 2.17 在文字中處理HTML與XML的實體

問題：

```
```

解法：

```
```

討論：

```
```

範例：

```Python
```

## 2.18 文字的單詞化(Tokenizing)

問題：

```
```

解法：

```
```

討論：

```
```

範例：

```Python
```

## 2.19 撰寫一個遞迴下降剖析器(Recursive Descent Parser)

問題：

```
```

解法：

```
```

討論：

```
```

範例：

```Python
```

## 2.20 在位元組字串上進行文字作業

問題：

```
```

解法：

```
```

討論：

```
```

範例：

```Python
```
