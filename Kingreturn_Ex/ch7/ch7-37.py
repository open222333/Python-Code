# 使用while重新設計 ch7_24.py
players = ['Curry', 'Jordan', 'dJames', 'Durant', 'Obama', 'Kevin', 'Lin']
n = int(input("請輸入人數 ＝ "))
if n > len(players):
    n = len(players)  # 列出人數不大於串列元素數
index = 0  # 索引
while index < len(players):  # index是否在串列長度範圍
    if index == n:  # 是否達到想列出的人數
        break
    print(players[index], end=" ")
    index += 1  # 索引index加1
