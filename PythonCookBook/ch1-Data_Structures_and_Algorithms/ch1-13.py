'''
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

'''
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
