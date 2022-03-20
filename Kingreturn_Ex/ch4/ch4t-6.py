# 輸入房屋坪數 輸出平方公尺 格式化到小數第一位
area = int(input("請輸入坪數："))
print("{0:^2.1f} 坪 = {1:^2.1f} 平方公尺".format(area, area * 3.305))
