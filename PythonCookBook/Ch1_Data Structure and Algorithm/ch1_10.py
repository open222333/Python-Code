'''
1.10 從一個序列中移除重複的項目並維持原有順序
問題：
消除一個序列(sequence)中重複的值(duplicate values)，但保留剩下項目的次序
解法：
若序列中的值事可雜湊的(hashable)，可使用一個集合(set)一個產生器(generator)解決。
若序列中的值是不可雜湊(unhashable)例如：dict，使用key引數指定一個能把序列項目轉為hashable型別的函式，使可偵測重複的值。
討論：
若只是想消除重複的項目，通常使用set即可解決，但此方式不表保留順序。
此訣竅使用一個產生器函式(generator function)，表示此函式非常通用。
舉例：讀取檔案並消除重複行。

此處key函式模仿類似功能的內建函式：sorted()、min()、max()。相關實例：1.8，1.13
'''


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
