'''
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

'''
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
