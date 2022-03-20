# 寫入數值資料
fn = 'ch14/out14_27.txt'
x = 100

with open(fn, 'w') as file_Obj:
    file_Obj.write(x)  # 直接輸入數值x產生錯誤
