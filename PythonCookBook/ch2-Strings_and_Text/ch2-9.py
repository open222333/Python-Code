'''
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

'''
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
