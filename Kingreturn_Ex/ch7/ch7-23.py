# 輸出一系列數字 break 指令
print("測試1")
for digit in range(1, 11):
    if digit == 5:
        break
    print(digit, end=", ")
print()
print("測試2")
for dight in range(0, 11, 2):
    if dight == 5:
        break
    print(dight, end=", ")
