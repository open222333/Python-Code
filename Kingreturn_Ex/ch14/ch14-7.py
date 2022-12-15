# 刪除指定path檔案的應用
import os

myfile = 'ch14/test.py'
# 如果myfile存在就刪除此檔案
if os.path.exists(myfile):
    os.remove(myfile)
    print("刪除%s檔案成功" % myfile)
else:
    print("%s檔案不存在" % myfile)
