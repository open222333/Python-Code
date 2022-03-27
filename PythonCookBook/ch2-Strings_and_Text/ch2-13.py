'''
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
'''

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
