# 河內塔問題

def hanoi(n, src, aux, dst):
    '''河內塔'''
    if n == 1:  # 河內塔終止條件
        print(f'移動圓盤{src} 從{aux}到{dst}')
    else:
        hanoi(n - 1, src, dst, aux)
        print(f'移動圓盤{src} 從{aux}到{dst}')
        hanoi(n - 1, aux, src, dst)


n = eval(input("輸入圓盤數量:"))
hanoi(n, 'A', 'B', 'C')
