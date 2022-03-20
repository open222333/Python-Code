# 測試閏年
print("判斷輸入年份是否為閏年")
year = input("請輸入年份：")
rem4 = int(year) % 4
rem100 = int(year) % 100
rem400 = int(year) % 400
if rem4 == 0:
    if rem100 != 0 or rem400 == 0:
        print("%s是閏年" % year)
    else:
        print("%s不是閏年" % year)
else:
    print("%s不是閏年" % year)
