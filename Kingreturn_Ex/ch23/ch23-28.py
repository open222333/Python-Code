# 重新設計ch23_2.py 直接在命令提示字元輸入地址
import sys
import webbrowser

print(sys.argv[0])
if len(sys.argv) > 1:
    address = " ".join(sys.argv[1:])
webbrowser.open('http://www.google.com.tw/maps/place/' + address)
