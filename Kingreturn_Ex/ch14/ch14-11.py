# 獲得特定檔案的大小 os.path.getsize()
import os

# 如果檔案在目前工作目錄下可以省略路徑
print(os.path.getsize("ch14/ch14_1.py"))
print(os.path.getsize(
    "/Users/lichengen/Library/Mobile Documents/com~apple~CloudDocs/KingReturnEx/ch14/ch14_1.py"))
