# 執行檔案複製的應用 copy(source,destination)
import shutil

shutil.copy("ch14/source.txt", "ch14/dest.txt")  # 目前工作目錄檔案複製
shutil.copy("ch14/source.txt", "ch14/Python")  # 目前工作目錄檔案複製到
shutil.copy("ch14/source.txt", "dest.txt")  # 不同工作目錄檔案複製
