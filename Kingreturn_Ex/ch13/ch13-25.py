# stdin物件 可搭配readline()方法 可以讀取螢幕輸入直到按下鍵盤Enter的字串
import sys

print("請輸入字串，輸入完成按Enter = ", end=" ")

msg = sys.stdin.readline()
print(msg)
