'''
2.11 剝除字串中不想要的字元
* 問題：想要剝除(strip)不想要的字元。
* 解法：strip() lstrip() rstrip()
* 討論：處理內部的空白，需使用replace()或正規表達式(reqular expression)
運算式lines = (line.strip() for line in f)，有效率的原因，不會先把資料讀到任何暫存器，只會建立一個迭代器(iterator)，而這個迭代器產出的每個文字行都會套用剝除動作。
'''
# 剔除空白
s = '    hello world \n'
result = s.strip()
print(result)

result = s.lstrip()
print(result)

result = s.rstrip()
print(result)

# 剝除給定字元
t = '-----hello====='
result = t.lstrip('-')
print(result)

result = t.rstrip('=')
print(result)
