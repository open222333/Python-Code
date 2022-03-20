def mymax(n1: int, n2: int):
    """比較後，輸出最大值"""
    if n1 > n2:
        return n1
    elif n2 > n1:
        return n2
    else:
        return '輸入的兩個數值一樣'


num1, num2 = eval(input("請輸入兩個整數："))
print(mymax(num1, num2))
