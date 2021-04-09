# finally :不管是否有異常都執行finally程式
def division(x, y):
    try:  # try - except 指令
        return x / y
    except:  # 捕捉所有異常
        print("異常發生")
    finally:  # 離開函數前先執行此程式碼
        print("階段任務完成")


print(division(10, 2))  # 列出10/2
print(division(5, 0))  # 列出5/0
print(division('a', 'b'))  # 列出'a'/'b'
print(division(6, 3))  # 列出6/3
