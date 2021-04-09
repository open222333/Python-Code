# 檔案與目錄的操作 mkdir/rmdir/remove/chdir
import os

mydir = 'ch14/testch14'
# 如果mydir不存在就建立此資料夾
if os.path.exists(mydir):
    print("已經存在%s" % mydir)
else:
    os.mkdir(mydir)
    print("建立%s資料夾成功" % mydir)
