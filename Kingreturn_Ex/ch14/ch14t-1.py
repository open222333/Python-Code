import os

target = input('請輸入要建立的資料夾名字(位置在ch14/train/內)：')
targetdir = 'ch14/train/' + target
if os.path.exists(targetdir):
    print("%s已經存在" % target)
else:
    print("%s目錄不存在" % target)
    os.mkdir(targetdir)
    print("建立此目錄")
