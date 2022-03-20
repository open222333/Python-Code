def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    if n2 == 0:
        print("除數不能為0")
    else:
        return n1 / n2


while True:
    n1, n2 = eval(input("請輸入2個數字："))
    print("%s + %s = %s" % (str(n1), str(n2), str(add(n1, n2))))
    print("%s - %s = %s" % (str(n1), str(n2), str(sub(n1, n2))))
    print("%s * %s = %s" % (str(n1), str(n2), str(mul(n1, n2))))
    print("%s / %s = %s" % (str(n1), str(n2), str(div(n1, n2))))
    flag = input("是否繼續？(y/n)")
    if flag == 'y' or flag == 'Y':
        continue
    else:
        break
print("結束")
