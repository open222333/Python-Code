# 使用enumuerate()重新設計ch7_43.py
scores = [21, 29, 18, 33, 12, 17, 26, 28, 15, 19]
# 解析enumuerate物件
for count, score in enumerate(scores, 1):  # 數值初始是1
    if score >= 20:
        print("場次%d：得分%d" % (count, score))
