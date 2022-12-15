# 更改目前工作目錄
import os

newdir = '/Users/lichengen/Library/Mobile Documents/com~apple~CloudDocs/KingReturnEx/ch14/Python'
currentdir = os.getcwd()
print('列出目前工作資料夾', currentdir)

# 如果newdir不存在就建立此資料夾
if os.path.exists(newdir):
    print("已經存在%s" % newdir)
else:
    os.mkdir(newdir)
    print("建立%s資料夾成功" % newdir)

# 將目前工作資料夾改至newdir
os.chdir(newdir)
print('列出目前工作資料夾', os.getcwd())

# 將目前工作資料夾返回
os.chdir(currentdir)
print('列出目前工作資料夾', os.getcwd())
