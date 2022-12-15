# 預測學費
tuition = 50000
year = 0
while tuition < 60000:
    tuition = int(tuition * 1.05)
    year += 1
print("經過%d年後學費會達到或超過60000元" % year)
