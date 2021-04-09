import os

totalsize = 0
totalnum = 0
targetDir = input("請輸入欲查詢的資料夾名稱：")
if os.path.exists(targetDir):
    for file in os.listdir(targetDir):
        print("檔案名：%s，大小為：%d" %
              (file, os.path.getsize(os.path.join(targetDir, file))))
        totalsize += os.path.getsize(os.path.join(targetDir, file))
        totalnum += 1
else:
    print("%s此目錄不存在" % targetDir)

print("--------------------")
print("檔案總數為：%d，總大小為：%d" % (totalnum, totalsize))
