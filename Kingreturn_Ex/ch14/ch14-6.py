# 使用rmdir刪除
import os

mydir = 'ch14/testch14'
# 如果mydir存在就刪除此資料夾
if os.path.exists(mydir):
    os.rmdir(mydir)
    print("刪除%s資料夾成功" % mydir)
else:
    print("%s資料夾不存在" % mydir)
