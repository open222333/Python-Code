zenofpython = '''The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''
zenofpython = zenofpython.lower()  # 轉為小寫
for ch in zenofpython:  # 移除標點符號
    if ch in '-!.,*':
        zenofpython = zenofpython.replace(ch, '')
zenofpython = zenofpython.split()  # 轉成串列
zenofpythonDict = {}  # 建立空字典
for word in zenofpython:
    if word in zenofpythonDict:
        zenofpythonDict[word] += 1  # 若單字已存在則加一
    else:
        zenofpythonDict[word] = 1  # 若第一次則新增
# 進行單字排序
sorted_zenofpythonDict = {}
for item in sorted(zenofpythonDict):
    sorted_zenofpythonDict[item] = zenofpythonDict[item]
print(sorted_zenofpythonDict)
