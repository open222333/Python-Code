# A串列:1,3,5,7...99
A = [n for n in range(1, 100, 2)]
# B串列  1到100的質數
B = []
for n in range(2, 101):
    # 2為質數
    if n == 2:
        B.append(n)
    # 判斷是否為質數
    for m in range(2, n):
        if n % m == 0:
            break
        elif m == n - 1:
            B.append(n)
A = set(A)
B = set(B)
print('A：', A)
print('B：', B)
print('A & B :', A & B)
print('A | B :', A | B)
print('A - B :', A - B)
print('B - A :', B - A)
print('AB對稱差集 :', A ^ B)
print('BA對稱差集 :', B ^ A)
