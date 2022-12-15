# 字典生成式
word = 'deepstone'
alphabetCount = {alphabet: word.count(alphabet) for alphabet in word}
print(alphabetCount)
