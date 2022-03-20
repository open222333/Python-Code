'''
2.8 為多行的模式撰寫一個正規表達式
* 問題：試著使用一個正規表達式(reqular expression)來比對一個區塊(block)，希望比對動作能夠跨越數行。
* 解法：正規表達式的. 不匹配換行字元(newline)。(?:.|\n)指定一個非捕捉組。
* 討論：re.compile() 接受一個旗標 re.DOTALL，用處：匹配所有字元，包含(newline)
'''
import re

comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a 
multiline comment */'''
result = comment.findall(text1)
print(result)
# 多行無法比對
result = comment.findall(text2)
print(result)

comment = re.compile(r'/\*((?:.|\n)*?)\*/')
result = comment.findall(text2)
print(result)

# 旗標 re.DOTALL，用處：匹配所有字元，包含(newline)
comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
result = comment.findall(text2)
print(result)
