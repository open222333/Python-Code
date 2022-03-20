'''
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

'''
import re
str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
text2 = 'Computer says "no." Phone says "yes."'
result = re.findall(str_pat, text1)
print(result)

str_pat_2 = re.compile(r'\"(.*?)\"')
result = str_pat_2.findall(text2)
print(result)
