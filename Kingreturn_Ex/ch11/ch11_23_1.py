# 傳遞任意數量的參數 驗證*toppings是元組
def make_icecream(*toppings):
    # 列出製作冰淇淋的配料
    print("這個所加配料如下")
    for topping in toppings:
        print("---", topping)
    print(type(toppings))
    print(toppings)


make_icecream('草莓醬')
make_icecream('草莓醬', '葡萄乾', '巧克力碎片')
