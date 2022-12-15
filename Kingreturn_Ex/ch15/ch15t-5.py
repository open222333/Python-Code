def division(x, y):
    try:
        return x / y
    except (ZeroDivisionError, TypeError):
        return '除數不能為0 或 輸入型態錯誤'


while True:
    x, y = eval(input('請輸入被除數,除數:'))
    print(division(x, y))
    tag = input("輸入任意值，若輸入Q或q離開:")
    if tag == 'q' or tag == 'Q':
        break
