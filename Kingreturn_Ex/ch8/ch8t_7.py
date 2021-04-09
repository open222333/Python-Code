total_people = (1100, 652, 946, 821, 955, 1024, 1155)
mean = sum(total_people) / len(total_people)
var = 0  # 變異值
for v in total_people:
    var += ((v - mean) ** 2)
var = var / (len(total_people) - 1)
dev = 0  # 標準差
for v in total_people:
    dev += ((v - mean) ** 2)
dev = (dev / (len(total_people) - 1)) ** 0.5
print("統一超商人數：\n平均值：%d\n變異數：%d\n標準差：%d" % (mean, var, dev))
