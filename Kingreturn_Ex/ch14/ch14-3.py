# 傳回特定路段相對路徑 os.path.relpath()
import os

print(os.path.relpath('/User')) #列出目前工作目錄到/User的相對路徑
print(os.path.relpath('ch14_3.py'))