# enumerate物件 使用for迴圈解析
scores = [21, 29, 18, 33, 12, 17, 26, 28, 15, 19]
# 不使用enumerate物件
index = 1
for score in scores:
    if score >= 20:
        print("場次%d：得分%d" % (index, score))
    index += 1
