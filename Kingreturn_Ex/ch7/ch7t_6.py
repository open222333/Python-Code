fahrenheilt = [32, 77, 104]  # 華氏溫度
celsius = []  # 攝氏溫度
for f in fahrenheilt:
    celsius.append((f - 32) * 5 / 9)
print(celsius)
