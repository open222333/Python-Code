# 房屋貸款實作
loan = eval(input("請輸入貸款金額："))
year = eval(input("請輸入年限："))
rate = eval(input("請輸入年利率："))
monthrate = rate / (12 * 100)  # 改成百分比 以及月利率
# 計算每月還款金額
molecules = loan * monthrate
denominator = 1 - (1 / (1 + monthrate) ** (year * 12))
monthlyPay = molecules / denominator  # 每月還款金額
totalPay = monthlyPay * year * 12  # 總共還款金額

print("每月還款金額：%d" % int(monthlyPay))
print("總共還款金額：%d" % int(totalPay))
