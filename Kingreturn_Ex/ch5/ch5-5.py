# 輸入數字 回應 A,B,C,D,F等級
print("最終成績計算系統")
score = input("請輸入分數：")
sc = int(score)
if sc >= 90:
    print('A')
elif sc >= 80:
    print('B')
elif sc >= 70:
    print('C')
elif sc >= 60:
    print('D')
else:
    print('F')
