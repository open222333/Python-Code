'''
## 1.16 過濾序列的元素

問題：

```
一個有資料的序列(sequence)，使用某些條件擷取出值，或縮減(reduce)該佇列。
```

解法：

```
串列概括式：過濾(filter)序列資料最容易的方式通常是使用一個串列概括式(list comprehension)。
產生器運算式：也可用產生器運算式(genrtator expressions)透過迭代動作逐次產生過濾後的值。
filter()函式：若過濾的程序涉及例外處理或其他繁複的細節，可使用內建的filter()函式。
```

討論：

```
串列概括式和產生器運算式通常過濾簡單資料最簡單也最直接的方式。有過濾同時轉換資料的額外功能。
以新的值取代不符合條件的值：將過濾條件一到一個條件運算式(conditional expression)。
itertools.compress()：接受一個可迭代物件(iterable)以及一個搭配的Boolean選擇器序列(selector sequence)作為輸入。
filter()和compress()都回傳一個迭代器(iterator)

```

'''
from itertools import compress
import math

# 串列概括式
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print(n for n in mylist if n > 0)
print(n for n in mylist if n < 0)

# 串列概括式和產生器運算式通常過濾簡單資料最簡單也最直接的方式。有過濾同時轉換資料的額外功能。
print([math.sqrt(n) for n in mylist if n > 0])

# 產生器運算式
pos = (n for n in mylist if n > 0)
print(pos)

for x in pos:
    print(x)

# filter()函式：若過濾的程序涉及例外處理或其他繁複的細節，可使用內建的filter()函式。
values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


ivals = list(filter(is_int, values))
print(ivals)

clip_neg = [n if n > 0 else 0 for n in mylist]
print(clip_neg)

clip_pop = [n if n < 0 else 0 for n in mylist]
print(clip_pop)
# itertools.compress()：接受一個可迭代物件(iterable)以及一個搭配的Boolean選擇器序列(selector sequence)作為輸入。
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5000 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE'
]

counts = [0, 3, 10, 4, 1, 7, 6, 1]
# 建立一個Boolean值序列
more5 = [n > 5 for n in counts]
print(more5)
# compress跳出對應True的值
print(list(compress(addresses, more5)))
