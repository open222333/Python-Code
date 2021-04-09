# 擲骰子遊戲
import random


def dice3gmae():  # 擲骰子
    dice = []  # 儲存
    for i in range(1, 4):
        i = random.choice([1, 2, 3, 4, 5, 6])
        dice.append(i)
    return dice


money = eval(input("請輸入賭金："))
while True:
    dice = dice3gmae()
    print("=========================================")
    print("輸入L或l表示大,輸入S或s表示小,輸入Q或q則程式結束")
    print("輸入數字3~18則猜骰子點數總和")
    print("大小賠1倍 猜點數賠10倍")
    print("=========================================")
    playerInput = input("骰子遊戲，請輸入：")
    # 避免規格外的輸入
    inputitem = ['3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13',
                 '14', '15', '16', '17', '18', 'Q', 'q', 'L', 'l', 'S', 's']
    if playerInput not in inputitem:
        print("請輸入規定的內容")
        continue
    playerBet = eval(input("請輸入賭注："))
    money -= playerBet  # 先從賭金內扣除賭注
    if playerInput == 'Q' or playerInput == 'q':
        break
    # 顯示骰子點數
    for i in range(3):
        print("第%d個骰子點數為：%d" % (i + 1, dice[i]))
    # 判斷輸贏
    if sum(dice) > 10:
        if playerInput == 'L' or playerInput == 'l':
            money += (playerBet * 2)
            print("恭喜贏的賭金：%d ,目前賭金為：%d" % (playerBet, money))
        else:
            print("輸掉的賭金：%d ,目前賭金為：%d" % (playerBet, money))
    elif sum(dice) <= 10:
        if playerInput == 'S' or playerInput == 's':
            money += (playerBet * 2)
            print("恭喜贏的賭金：%d ,目前賭金為：%d" % (playerBet, money))
        else:
            print("輸掉的賭金：%d ,目前賭金為：%d" % (playerBet, money))
    elif sum(dice) == int(playerInput):
        money += (playerBet * 11)
        print("恭喜贏的賭金：%d ,目前賭金為：%d" % (playerBet * 10, money))
    else:
        print("輸掉的賭金：%d ,目前賭金為：%d" % (playerBet, money))
    # 賭金沒了結束程式
    if money <= 0:
        break
