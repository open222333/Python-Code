import unicodedata
import sys


'''
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
'''

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
