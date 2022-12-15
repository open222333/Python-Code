# while迴圈 break指令
msg1 = '人機對話專欄,請告訴我你喜歡吃的水果！'
msg2 = '輸入 q 可以結束對話'
msg = msg1 + '\n' + msg2 + '\n' + '= '
while True:  # 這是while無限迴圈
    input_msg = input(msg)
    if input_msg == 'q':  # 如果輸入不是q才輸出訊息
        break
    else:
        print("我也喜歡吃%s" % input_msg.title())
