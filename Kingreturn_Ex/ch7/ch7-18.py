# 畢達哥拉斯直角三角形 列出0-19符合此定義的組合
x = [[a, b, c] for a in range(1, 20) for b in range(a, 20)
     for c in range(b, 20) if a ** 2 + b ** 2 == c ** 2]
print(x)
