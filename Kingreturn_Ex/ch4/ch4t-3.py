# 重新設計cht4_2.py 將結果輸出在out.txt
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # 將目前檔案位置設為工作目錄

outfile = open(file="out.txt", mode="w")
outfile.write('姓名 國文 英文 總分 平均\n')
outfile.write('%3s %4d %4d %4d %4.1f\n' % ('洪冰儒', 98, 90, 188, (98 + 90) / 2))
outfile.write('%3s %4d %4d %4d %4.1f\n' % ('洪雨星', 96, 95, 191, (96 + 95) / 2))
outfile.write('%3s %4d %4d %4d %4.1f\n' % ('洪冰雨', 92, 88, 180, (92 + 88) / 2))
outfile.write('%3s %4d %4d %4d %4.1f\n' % ('洪星宇', 93, 97, 190, (93 + 97) / 2))
outfile.close()
