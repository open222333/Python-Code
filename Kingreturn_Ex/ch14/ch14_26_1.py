# 重新設計 ch14_26.py 傳回資料長度
fn = 'ch14/out14_26.txt'
string = 'I love Python.'

with open(fn, 'w') as file_Obj:
    print(file_Obj.write(string))
