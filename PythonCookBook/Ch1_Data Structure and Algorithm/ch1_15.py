'''
1.15 基於一個欄位來為記錄分組
問題：
一個由字典(dictionaries)或實體(instances)所構成的序列，基於一個特定欄位(例如日期)的值來分組迭代(iterate over)資料。
解法：
itertools.groupby()函式適用。
討論：
groupby()函式的運作方式是掃瞄一個序列，尋找連續出現的相同值(或由給定的key函式索回傳得值)加以歸組。
每次迭代中，會回傳那個值以及一個迭代器(iterator)。
第一部需依據要分組的欄位進行排序，因groupby()只檢視連續的項目。
若目標是將資料依照日期歸組，成為一個可隨機存取的大型資料結構。
使用defaultdict()建置一個multidict(訣竅1.6)
'''
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
