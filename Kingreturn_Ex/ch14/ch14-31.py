# 附加文件內容 添加內容不覆蓋 mode = a
fn = 'ch14/out14_31.txt'
str1 = 'I love Python.'
str2 = 'Learn Python from the best book.'

with open(fn, 'a') as file_Obj:
    file_Obj.write(str1 + '\n')
    file_Obj.write(str2 + '\n')
