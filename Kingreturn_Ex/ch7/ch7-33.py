# Sentinel value 哨兵值:迴圈結束執行的值
n = int(input("請輸入一個值："))
sum = 0
while n != 0:  # 哨兵值是0
    sum += n
    n = int(input("請輸入一個值："))
print("輸入總和 ＝ ", sum)
