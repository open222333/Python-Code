'''
1.12 找出一個序列中出現最頻繁的項目
問題：
有一個由項目所構成的序列，找出出現最頻繁的項目
解法：
collections.Counter類別的most_common()方法
討論：
Counter物件可接受任何可雜湊(hashable)的項目序列作為輸入。
Counter是一個映射到出現次數的字典。
若要手動增加次數可用加法。也能使用update()方法。
Counter可用各種數學運算。
Counter物件對於任何需要用到表格資料並進行技術的問題是非常實用的工具。
'''
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
