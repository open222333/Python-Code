def reverse(n: int):
    """反向顯示數字"""
    newn = ''
    for i in str(n):
        newn = i + newn
    return int(newn)

num = int(input("請輸入正整數："))
print(reverse(num))