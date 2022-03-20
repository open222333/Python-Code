'''
2.1 依據任意的多個定界符來切分字串
* 問題：需要把一個字串切分(split)成幾個欄位，但字串中界定欄位的定介符(delimiters)以及其周圍的空白數並不一致。
* 解法：字串的split()可解決，若要更多彈性，則可使用re.split()。
* 討論：re.split()
*   若正則表達式中含有用括號(parentheses)包圍的捕捉組(capture group)，匹配的文字也會出現在結果中。
'''
import re
line = 'asdf fjdk; afed, fjek,asdf, foo'
print(re.split(r'[;,\s]\s*', line))

# 若正則表達式中含有用括號(parentheses)包圍的捕捉組(capture group)，匹配的文字也會出現在結果中。
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)

values = fields[::2]
delimiters = fields[1::2] + ['']
print(values)
print(delimiters)

# 使用相同的定界符重新格式化這個文字行
a = ''.join(v + d for v, d in zip(values, delimiters))
print(a)

b = re.split(r'(?:,|;|\s)\s*', line)
print(b)
