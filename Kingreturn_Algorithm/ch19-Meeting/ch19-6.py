# 雞兔同籠
chicken = 0
while True:
    rabbit = 35 - chicken  # 頭的總數
    if 2 * chicken + 4 * rabbit == 100:  # 腳的總數
        print('幾有{}隻, 兔有{}隻'.format(chicken, rabbit))
        break
    chicken += 1
