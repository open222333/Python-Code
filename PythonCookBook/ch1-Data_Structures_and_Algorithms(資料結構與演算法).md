# ch1-Data_Structures_and_Algorithms(資料結構與演算法)

## 目錄

- [ch1-Data_Structures_and_Algorithms(資料結構與演算法)](#ch1-data_structures_and_algorithms資料結構與演算法)
	- [目錄](#目錄)
- [內容](#內容)
	- [1.1 將一個序列拆分給個別變數](#11-將一個序列拆分給個別變數)
	- [1.2 拆解一個任意長度的可迭代物件之元素](#12-拆解一個任意長度的可迭代物件之元素)
	- [1.3 留下最後Ｎ個項目](#13-留下最後ｎ個項目)
	- [1.4 找出最大或最小的Ｎ個項目](#14-找出最大或最小的ｎ個項目)
	- [1.5 實作一個優先序佇列](#15-實作一個優先序佇列)
	- [1.6 在一個字典中將鍵值映射至多個值](#16-在一個字典中將鍵值映射至多個值)
	- [1.7 維持字典的秩序](#17-維持字典的秩序)
	- [1.8 以字典進行運算](#18-以字典進行運算)
	- [1.9 找出兩個字典的共通處](#19-找出兩個字典的共通處)
	- [1.10 從一個序列中移除重複的項目並維持原有順序](#110-從一個序列中移除重複的項目並維持原有順序)
	- [1.11 為一個切片(Slice)命名](#111-為一個切片slice命名)
	- [1.12 找出一個序列中出現最頻繁的項目](#112-找出一個序列中出現最頻繁的項目)
	- [1.13 藉由一個共通的鍵值來排序一個由字典所構成的串列](#113-藉由一個共通的鍵值來排序一個由字典所構成的串列)
	- [1.14 在不支援原生的比較運算的情形下排序物件](#114-在不支援原生的比較運算的情形下排序物件)
	- [1.15 基於一個欄位來為記錄分組](#115-基於一個欄位來為記錄分組)
	- [1.16 過濾序列的元素](#116-過濾序列的元素)
	- [1.17 擷取出一個字典的子集合](#117-擷取出一個字典的子集合)
	- [1.18 將名稱映射至序列元素](#118-將名稱映射至序列元素)
	- [1.19 同時轉換並縮減資料](#119-同時轉換並縮減資料)
	- [1.20 將多個映射結合為單一映射](#120-將多個映射結合為單一映射)

# 內容

## 1.1 將一個序列拆分給個別變數

問題：

```
有一個Ｎ個元素的元組(tuple)或序列(sequen),拆分給Ｎ個變數
```

解法：

```
賦值(assignment operation) 拆分給變數
```

討論：

```
拆分(unpacking)可用在任何可迭代物件(iterable)：元組 串列 字串 檔案 迭代器(iterators) 產生器(generators)
用了就丟的變數名稱(throwaway variable name)：_，須確保所挑的名稱沒用在其他地方
```

範例：

```python
# 將一個序列拆分給個別變數
p = (4, 5)
x, y = p
print(x)
print(y)


data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print(name)
print(date)

name, shares, price, (year, mon, day) = data
print(year)
print(mon)
print(day)

# 結論
# 拆分(unpacking)可用在任何可迭代物件(iterable)
# 元組 串列 字串 檔案 迭代器(iterators) 產生器(generators)
s = "hello"
a, b, c, d, e = s
print(a)
print(b)
print(c)

# 拆分時 丟棄某些值
data = ['ACME', 50, 91.1, (2012, 12, 21)]
_, shares, price, _ = data
print(shares)
print(price)
```

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

範例：

```Python
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
```

## 1.3 留下最後Ｎ個項目

問題：

```
在迭代(iteration)或某種處理動作的過程中留下最近項目的少量歷程紀錄(limited history)
```

解法：

```
collections.deque適合用來製作這種少量的歷程紀錄。
```

討論：

```
搜尋特定項目(items)時，通常使用yield的產生器函示(generator function)
```

範例：

```Python
# 留下最後N個項目
# 在迭代(iteration) 或某種處理動作的過程中留下最近幾個項目的少量歷程紀錄(limited history)

from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


# 在一個檔案上的使用範例
if __name__ == '__main__':
    with open('somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)

# 搜尋特定項目時 常用yield產生器函式
q = deque(maxlen=3)  # deque(maxlen=N) 產生固定佇列 新的項目加入 佇列已滿 舊的會移除
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)

q.appendleft(4)
q.popleft()
```

## 1.4 找出最大或最小的Ｎ個項目

問題：

```
找出一個群集(collection)中最大或最小的Ｎ個項目做成一個串列(list)
```

解法：

```
heapq模組 nlargest() nsmallest()
```

討論：

```
heapq運作方式：先將資料轉為一個串列，項目以堆積(heap)的形式安置的。
若找單一最大最小 使用max() min()
若Ｎ的大小接近該群集 使用sorted(items)[:N] sorted(item)[-N:]
```

範例：

```Python
import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))
heap = list(nums)
heapq.heapify(heap)
print(heapq.heappop())  # 取出第一個項目

portfollo = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, portfollo, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfollo, key=lambda s: s['price'])
```

## 1.5 實作一個優先序佇列

問題：

```
實作一個佇列(queue)，依據給定的優先序(priority)排序項目，每次取出(pop)都回傳最高優先序的項目
```

解法：

```
用heapq模組實作簡單的優先序佇列
```

討論：

```
heapq.heappush() 插入項目
heapq.heappop() 回傳那個最小的項目
佇列由(-priority, index, item)這種形式的元組(tuples)，取負的priority使項目從最高優先序排到最低優先序
Item實體(instances)是無法比較。
(priority, item)元組，可比較，若有相同優先序就會無法比較。
(priority, index, item)可以比較且因元組不會有相同的index，不會有無法比較的問題。
若要將此佇列用在執行緒(threads)之間的通訊，得加入適當的鎖定(locking)與訊號(signaling)機制。
```

範例：

```Python
import heapq

class ProiorityQueue:
    '''用heapq模組實作簡單的優先序佇列'''

    def __init__(self) -> None:
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


# 使用ProiorityQueue
class Item:
    def __init__(self, name) -> None:
        self.name = name

    def __repr__(self) -> str:
        return 'Item({!r})'.format(self.name)


q = ProiorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())

# Item實體無法比較
a = Item('foo')
b = Item('bar')
# print(a < b) # 出現錯誤

# (priority, item)元組，可比較，若有相同優先序就會無法比較。
a = (1, Item('foo'))
b = (5, Item('bar'))
print(a < b)
c = (1, Item('grok'))
# 若有相同優先序就會無法比較。
# print(a < c) # 出現錯誤

# (priority, index, item)可以比較且因元組不會有相同的index，不會有無法比較的問題。
a = (1, 0, Item('foo'))
b = (5, 1, Item('bar'))
c = (1, 2, Item('grok'))
print(a < b)
print(a < c)

```

## 1.6 在一個字典中將鍵值映射至多個值

問題：

```
製作一個字典，將各個鍵值(keys)映射到一個以上的值(multidict)
```

解法：

```
將值使用串列或集合儲存。
串列：保留插入順序
集合：移除重複項目
可使用collections模組中的defaultdict：自動初始化第一個值，可專注在值的新增。會自動建立字典條目(dictionary entries)
若不想要自動建立字典條目，可使用setdefult()
```

討論：

```
使程式碼更簡潔
```

範例：

```Python
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)

d2 = defaultdict(set)
d2['a'].add(1)
d2['a'].add(2)
d2['b'].add(4)
print(d2)

d3 = {}
d3.setdefault('a', []).append(1)
d3.setdefault('a', []).append(2)
d3.setdefault('b', []).append(4)

pairs = {1: 'a', 2: 'b.'}

d4 = {}
for key, value in pairs:
    if key not in d4:
        d4[key] = []
    d[key].append(value)

d5 = defaultdict(list)
for key, value in pairs:
    d5[key].append(value)
```

## 1.7 維持字典的秩序

問題：

```
建立一個字典(dictionary)，且在迭代(iterating)或序列化(serializing)時，控制其中項目的次序。
```

解法：

```
collection模組的OrderedDict:在迭代時完全保留資料插入順序。
若想精準控制JSON編碼中欄位出現的順序，可先建立一個裝有資料的OrderedDict。
```

討論：

```
OrderedDict在內部維護一個雙向鏈結串列(doubly linked list)，依照插入的次序來安排鍵值的次序。
一個OrderedDict的大小超過一個正常字典的兩倍大，因創建了額外的鏈結串列。
```

範例：

```Python
from collections import OrderedDict
import json


d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for key in d:
    print(key, d[key])

# 若想精準控制JSON編碼中欄位出現的順序，可先建立一個裝有資料的OrderedDict。
print(json.dumps(d))
```

## 1.8 以字典進行運算

問題：

```
在一個資料字典(dictionary)，進行各種運算。
```

解法：

```
使用zip()反轉(invert)這個鍵值的keys與values。
使用zip()搭配sorted()進行排序。
注意：zip()建立一個只能消耗一次的迭代器(iterator)
```

討論：

```
若在字典進行常見的資料縮簡(data reductions)，只會處理鍵值(keys)。
zip()反轉成(values,keys)的序列，先比較value，若剛好有一樣的值，會比較鍵值(key)。
```

範例：

```Python
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))

print(min_price)
print(max_price)

prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)

# 以下會出錯 注意：zip()建立一個只能消耗一次的迭代器(iterator)
prices_and_names = zip(prices.values(), prices.keys())
print(max(prices_and_names))  # OK
try:
    print(min(prices_and_names))  # ValueError: min() arg is an empty sequence
except Exception as err:
    print(err)

# 若在字典進行常見的資料縮簡(data reductions)，只會處理鍵值(keys)。
min(prices)
max(prices)

min(prices.values())
max(prices.values())

# 可回傳正確資料
min(prices, key=lambda k: prices[k])
max(prices, key=lambda k: prices[k])

# 取得值須額外處理
min_value = prices[min(prices, key=lambda k:prices[k])]

# zip()反轉成(values,keys)的序列，先比較value，若剛好有一樣的值，會比較鍵值(key)。
prices = {'AAA': 45.23, 'ZZZ': 45.23}
print(min(zip(prices.values(), prices.keys())))
print(max(zip(prices.values(), prices.keys())))
```

## 1.9 找出兩個字典的共通處

問題：

```
找出兩個字典共通的鍵值(keys)、值(values)
```

解法：

```
使用keys()或item()做簡單的集合運算(set operations)，這類運算也這類運算也可用來更動或過濾字典的內容。
```

討論：

```
一個字典就是一個鍵值(key)集合與一個值(value)集合之間的映射(mapping)。
字典的keys()會回傳一個揭露這些鍵值的keys-view物件。這些物件支援集合運算。
字典的items()會回傳一個items-view物件，由(key, value)對組構成。這些物件支援集合運算。
字典的values()不支援集合運算。原因：values-view 值不保證唯一，使得某些集合運算失去功用。
```

範例：

```Python
a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

# 使用keys()或item()做簡單的集合運算(set operations)，這類運算也這類運算也可用來更動或過濾字典的內容。
# 找出共通的鍵值(keys)
print(a.keys() & b.keys())
# 找出在a但不在b的鍵值
print(a.keys() - b.keys())
# 找出共通的對組
print(a.items() & b.items())

# 製作一個特定鍵值被移除的新字典
c = {key: a[key] for key in a.keys() - {'z', 'w'}}
print(c)
```

## 1.10 從一個序列中移除重複的項目並維持原有順序

問題：

```
消除一個序列(sequence)中重複的值(duplicate values)，但保留剩下項目的次序
```

解法：

```
若序列中的值事可雜湊的(hashable)，可使用一個集合(set)一個產生器(generator)解決。
若序列中的值是不可雜湊(unhashable)例如：dict，使用key引數指定一個能把序列項目轉為hashable型別的函式，使可偵測重複的值。
```

討論：

```
若只是想消除重複的項目，通常使用set即可解決，但此方式不表保留順序。
此訣竅使用一個產生器函式(generator function)，表示此函式非常通用。
舉例：讀取檔案並消除重複行。

此處key函式模仿類似功能的內建函式：sorted()、min()、max()。相關實例：1.8，1.13
```

範例：

```Python
def dedupe_hashable(items):
    # 若序列中的值事可雜湊的(hashable)，可使用一個集合(set)一個產生器(generator)解決。
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


def dedupe_unhashable(items, key=None):
    # 若序列中的值是不可雜湊(unhashable)例如：dict，使用key引數指定一個能把序列項目轉為hashable型別的函式，使可偵測重複的值。
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe_hashable(a)))

# 若只是想消除重複的項目，通常使用set即可解決，但此方式不表保留順序。
print(set(a))

a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
print(list(dedupe_unhashable(a, key=lambda d: (d['x'], d['y']))))
print(list(dedupe_unhashable(a, key=lambda d: d['x'])))

# 舉例：讀取檔案並消除重複行。
with open('somefile', 'r') as f:
    for line in dedupe_unhashable(f):
        pass
```

## 1.11 為一個切片(Slice)命名

問題：

```
若清理程式充斥著寫死(hardcoded)在程式碼中的切片索引(slice indices)
```

解法：

```
程式碼範例
```

討論：

```
內建的slice()會建立一個slice物件，可用在任何允許切片(slice)的地方。
假設有個slice實體s，可用s.start、s.stop、s.step取得更多資訊。
可使用indices(size)會回傳(start, stop, step)元組(tuple)。
```

範例：

```Python
# 0123456789012345678901234567890123456789012345678901234567890123456789
record = '....................100          .......513.25     ..........'
cost = int(record[20:32]) * float(record[40:48])
print(cost)

# 內建的slice()會建立一個slice物件，可用在任何允許切片(slice)的地方。
items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print(items[2:4])
print(items[a])
items[a] = [10, 11]
print(items)
del items[a]
print(items)

# 可使用indices(size)會回傳(start, stop, step)元組(tuple)。
a = slice(5, 50, 2)
print(a.start)
print(a.stop)
print(a.step)

s = 'HelloWorld'
a.indices(len(s))
for i in range(*a.indices(len(s))):
    print(s[i])
```

## 1.12 找出一個序列中出現最頻繁的項目

問題：

```
有一個由項目所構成的序列，找出出現最頻繁的項目
```

解法：

```
collections.Counter類別的most_common()方法
```

討論：

```
Counter物件可接受任何可雜湊(hashable)的項目序列作為輸入。
Counter是一個映射到出現次數的字典。
若要手動增加次數可用加法。也能使用update()方法。
Counter可用各種數學運算。
Counter物件對於任何需要用到表格資料並進行技術的問題是非常實用的工具。
```

範例：

```Python
from collections import Counter
words = ['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'the', 'eyes',
         'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into', 'my', 'eyes', "you're", 'under']

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)

print(word_counts['not'])
print(word_counts['eyes'])

morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
# 以下等於 word_counts.update(morewords)
for word in morewords:
    word_counts[word] += 1
print(word_counts['eyes'])

a = Counter(words)
b = Counter(morewords)
print(a)
print(b)

# 結合次數
c = a + b
print(c)

# 減去次數
d = a - b
print(d)
```


## 1.13 藉由一個共通的鍵值來排序一個由字典所構成的串列

問題：

```
一個字典串列(a list of dictionaries)，依據一或多個字典的直來排序其中的條目(entries)。
```

解法：

```
使用operator模組的itemgetter函式，能輕鬆排序這種結構。
```

討論：

```
operation.itemgetter()函式可接受的引數是可被用來從rows中的記錄擷取出想要的值的查找索引(lookup indices)，可以是字典鍵值名稱、串列元素或可被未入一個物件的__getitem__()方法的任何值。
若給itemgetter()多個索引，所產的的可呼叫物件會回傳一個其中含有所有指定的值的元組，而sorted()會依據這些元組的次序輸出。
itemgetter()的功能可用lambda取代，但itemgetter()會跑得快一點。若有效能考量可使用。
```

範例：

```Python
from operator import itemgetter

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_fname)
print(rows_by_uid)

# itemgetter() 能接受多個鍵值
rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print(rows_by_lfname)

# itemgetter()可用lambda取代
rows_by_fname = sorted(rows, key=lambda k: k['fname'])
rows_by_uid = sorted(rows, key=lambda k: k['uid'])
print(rows_by_fname)
print(rows_by_uid)
```

## 1.14 在不支援原生的比較運算的情形下排序物件

問題：

```
想排序(sort)同一類別(class)的物件，但沒原生支援(natively support)的比較運算可用。
```

解法：

```
內建的sorted()函式接受一個key引數，可藉此傳入一個可呼叫物件(callable)，這個callable會回傳物件中的某些值，而sorted會用這些值來比較物件。
可使用lambda以及operator.attrgetter()
```

討論：

```
可使用lambda以及operator.attrgetter()，attrgetter()速度通常較快一點，且多了「允許同時擷取出多個欄位」的功能。類似為字典使用operator.itemgetter()的選擇(訣竅1.13)。
也可套用到min()或max()這樣的函式。
```

範例：

```Python
from operator import attrgetter


class User:
    def __init__(self, user_id) -> None:
        self.user_id = user_id

    def __repr__(self) -> str:
        return 'User({})'.format(self.user_id)


users = [User(23), User(3), User(99)]
print(users)
# 可使用lambda以及operator.attrgetter()
print(sorted(users, key=lambda u: u.user_id))
print(sorted(users, key=attrgetter('user_id')))

# attrgetter()速度通常較快一點，且多了「允許同時擷取出多個欄位」的功能。
by_name = sorted(users, key=attrgetter('last_name', 'first_name'))
print(by_name)

# 也可套用到min()或max()這樣的函式。
print(min(users, key=attrgetter('user_id')))
print(max(users, key=attrgetter('user_id')))
```

## 1.15 基於一個欄位來為記錄分組

問題：

```
一個由字典(dictionaries)或實體(instances)所構成的序列，基於一個特定欄位(例如日期)的值來分組迭代(iterate over)資料。
```

解法：

```
itertools.groupby()函式適用。
```

討論：

```
groupby()函式的運作方式是掃瞄一個序列，尋找連續出現的相同值(或由給定的key函式索回傳得值)加以歸組。
每次迭代中，會回傳那個值以及一個迭代器(iterator)。
第一部需依據要分組的欄位進行排序，因groupby()只檢視連續的項目。
若目標是將資料依照日期歸組，成為一個可隨機存取的大型資料結構。
使用defaultdict()建置一個multidict(訣竅1.6)
```

範例：

```Python
from collections import defaultdict
from itertools import groupby
from operator import itemgetter

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5000 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'}
]

# 先依想要的欄位排序
rows.sort(key=itemgetter('date'))
# 分組進行迭代
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print('     ', i)

# 若目標是將資料依照日期歸組，成為一個可隨機存取的大型資料結構。
# 可節省記憶體
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)

for r in rows_by_date['07/01/2012']:
    print(r)
```

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

範例：

```Python
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
```

## 1.17 擷取出一個字典的子集合

問題：

```
製作一個字典，為另個字典的子集(subset)
```

解法：

```
使用字典概括式(dictionary comprehension)能夠輕易達成目標。
```

討論：

```
建立一個元組序列(a sequen of tuples)並傳給dict函式。也可達成字典概括能做到的大部分事情。
```

範例：

```Python
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# 找出所有股價大於200的股票做成一個字典
p1 = {key: value for key, value in prices.items() if value > 200}

# 製作一個科技股字典
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key: value for key, value in prices.items() if key in tech_names}

# 建立一個元組序列(a sequen of tuples)並傳給dict函式。也可達成字典概括能做到的大部分事情。
# 但速度較慢
p3 = dict((key, value) for key, value in prices.items() if value > 200)

p4 = {key: prices[key] for key in prices.keys() if key in tech_names}
```

## 1.18 將名稱映射至序列元素

問題：

```
有段程式碼會依據位置存取串列(list)或元組(tuple)的元素，想用名稱存取元素，使結構少依賴位置。
```

解法：

```
collection.namedtuple()。
```

討論：

```
nametuple：可以用來取代字典，因字典所需儲存空間較大。然而不同於字典的是，nametuple的內容不可變(immutable)。
若需要變更屬性，可通過nametuple實體的_replace()方法，會建立一個全新的nametuple。
_replace()巧妙的用途：填充(populate)，具有選擇性欄位或缺少欄位的具名元組。
先製作一個有預設值的原型元組，然後用_replace()建立一個植被取代的新實體。
若是定義一種有效率的資料結構，可以考慮使用__slots__定義一個類別。(訣竅 8.4)
```

範例：

```Python
from collections import namedtuple


Subscriber = namedtuple('Subcriber', ['addr', 'joined'])
sub = Subscriber('jones@example.com', '2012-10-19')
print(sub)
print(sub.addr)
print(sub.joined)
print(len(sub))
addr, joined = sub
print(addr)
print(joined)

# 具名元組(named tuples) 一個主要用途：讓程式碼可以與操作的元素之位置分離。


def compute_cost(records):
    # 使用普通元組的程式碼
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total


Stock = namedtuple('Stock', ['name', 'shares', 'price'])


def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total


s = Stock('ACME', 100, 123.45)
print(s)
# s.shares = 75 # AttributeError: can't set attribute 發生錯誤
s = s._replace(shares=75)
print(s)

# _replace()巧妙的用途：填充(populate)，具有選擇性欄位或缺少欄位的具名元組。先製作一個有預設值的原型元組，然後用_replace()建立一個植被取代的新實體。
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])

# 建立一個原形實體
stock_prototype = Stock('', 0, 0.0, None, None)

# 用來將字典轉為Stock的函式


def dict_to_stock(s):
    return stock_prototype._replace(**s)


a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
print(dict_to_stock(a))

b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
print(dict_to_stock(b))
```

## 1.19 同時轉換並縮減資料

問題：

```需要執行一個縮減函式(reduction function，例如：sum(),min(),max())，但得先轉換或過濾資料。
```

解法：

```
結合資料縮減動作和轉換動作的方式是使用產生器運算式引數(generator-expression argument)。
```

討論：

```
```

範例：

```Python
# 計算平方和
import os


nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)

# 判斷一個目錄中是否含有任何.py檔案
files = os.listdir('dirname')
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python.')

# 將一個元組輸出為CSV
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

# 跨越一個資料結構的欄位縮減資料
portfollo = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
min_shares = min(s['shares'] for s in portfollo)

s = sum((x * x for x in nums))  # 傳入 generator-expr 作為引數
s = sum(x * x for x in nums)  # 較為優雅的語法

s = sum([x * x for x in nums])  # 也可正常，但若資料量大，會創造出一個只用一次的大型暫存資料結構。

# 原本：回傳20
min_shares = min(s['shares'] for s in portfollo)
print(min_shares)

# 替代解法：回傳{'name':'', 'shares':20}
min_shares = min(portfollo, key=lambda s: s['shares'])
print(min_shares)
```

## 1.20 將多個映射結合為單一映射

問題：

```
有多個字典(dictionaries)或映射(mappings)，要合理的方式將他們結合，已進行某種動作，例如：值得查找或檢查鍵值是否存在。
```

解法：

```
collrctions模組的ChainMap類別。
```

討論：

```
ChainMap 若有變動都會變動第一個映射的值。
ChainMap特別適合用於具有範疇的值(scoped values，如全域值、區域值等)
作為ChainMap的替代方案，可以考慮使用update()方法將字典合併合併再一起。
```

範例：

```Python
from collections import ChainMap


a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

c = ChainMap(a, b)
print(c['x'])
print(c['y'])
# 先在a找 a沒有再到b找
print(c['z'])

print(len(c))
print(list(c.keys()))
print(list(c.values()))

c['z'] = 10
c['w'] = 40
del c['x']
print(a)
# del c['y']  # 出現錯誤

values = ChainMap()
values['x'] = 1
# 新增一個映射
values = values.new_child()
values['x'] = 2
# 新增一個映射
values = values.new_child()
values['x'] = 3
print(values)
print(values['x'])

# 丟棄最後一個映射
values = values.parents
print(values['x'])

# 丟棄最後一個映射
values = values.parents
print(values['x'])

print(values)

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = dict(b)
merged.update(a)
print(merged)
print(merged['x'])
print(merged['y'])
print(merged['z'])

a['x'] = 13
print(merged['x'])

merged = ChainMap(a, b)
print(merged['x'])
a['x'] = 42
print(merged['x'])
```
