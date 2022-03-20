'''
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

'''

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
