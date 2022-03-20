# 專題 質數 Prime Number
def is_Prime(num):
    for n in range(2, num):
        if num % n == 0:
            return False
        return True


num = int(input("請輸入大於1的整數做質數測試 ＝ "))
if is_Prime:
    print("%d是質數" % num)
else:
    print("%d不是質數" % num)
