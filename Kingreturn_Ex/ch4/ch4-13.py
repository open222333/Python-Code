#  輸出資料到檔案 將資料輸出到檔案的實例
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # 將目前工作目錄設定為指令搞所在目錄
fstream1 = open("out1.txt", mode="w")  # 取代先前資料
print("Testing for output", file=fstream1)
fstream1.close()
fstream2 = open("out2.txt", mode="a")  # 附加在資料後面
print("Testing for output", file=fstream2)
fstream2.close()
