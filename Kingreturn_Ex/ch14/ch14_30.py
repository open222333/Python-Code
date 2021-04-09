# 重新設計ch14_29.py 新增換行符號
fn = 'ch14/out14_30.txt'
str1 = 'I love Python.'
str2 = 'Learn Python from the best book.'

with open(fn, 'w') as file_Obj:
    file_Obj.write(str1 + '\n')
    file_Obj.write(str2 + '\n')
