maximum_temperature = (30, 28, 29, 31, 33, 35, 32)
minimum_temperature = (20, 21, 19, 22, 23, 24, 20)
sum = 0
for i in maximum_temperature:
    sum += i
for j in minimum_temperature:
    sum += j
avg = sum / (len(maximum_temperature) + len(minimum_temperature))
print("過去一週：\n最高溫：%d\n最低溫：%d\n平均溫：%.2f" %
      (max(maximum_temperature), min(minimum_temperature), avg))
