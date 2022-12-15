# 寫入檔案 將執行結果寫入空的文件內
fn = 'ch14/out14_26.txt'
string = 'I love Python.'

with open(fn, 'w') as file_Obj:
    file_Obj.write(string)
