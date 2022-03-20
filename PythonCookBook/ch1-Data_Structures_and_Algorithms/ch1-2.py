'''
## 1.2 拆解一個任意長度的可迭代物件之元素

問題：

```
解開一個可迭代物件(iterable)取出Ｎ個元素，但這個可疊愛物件的長度可能比Ｎ個元素還多，導致「要拆解的值太多(too many values to unpack)」的例外
```

解法：

```
星號運算式(star expressions)
```

討論：

```
延伸式的可迭代物件(extended iterable unpacking)動作專門用來拆解任意長度或長度未知的可迭代物件(iterables)
```

'''
# 拆解一個任意長度的可迭代物件之元素
# 星號運算式(star expressions)
def drop_frist_last(grades):
    first, *middle, last = grades
    return middle


user_record = ('Dave', 'deve@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = user_record
print(name)
print(email)
print(phone_numbers)  # 串列

# 最近一季與前七季相比
# *trailing, current = sales_record
# trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)
# return avg_comparison
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailing)
print(current)

# 討論
# 延伸式的可迭代物件拆解(extended iterable unpacking) 拆分任意長度或長度未知的可迭代物件
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4)
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)


# 切分(splitting)
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)
print(homedir)
print(sh)

# 用完即丟變數名稱(throwaway variable name) _ ign(代表ignored)
record = ('ACME', 50, 123.45, (12, 18, 2012))
head, *_, (*_, year) = record
print(name)
print(year)

# 拆解串列
items = [1, 10, 7, 4, 5, 9]
head, *tail = items
print(head)
print(tail)

# 遞迴演算法


def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head


print(sum(items))
