def division(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return '除數不能為0'
    except TypeError:
        return '輸入內容型態錯誤'


x, y = eval(input('請輸入被除數,除數(使用,隔開):'))
print(division(x, y))
