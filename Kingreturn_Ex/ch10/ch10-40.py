# 集合增加程式效率
word = 'deepstone'
alphabetCount = {alphabet: word.count(alphabet) for alphabet in set(word)}
print(alphabetCount)
