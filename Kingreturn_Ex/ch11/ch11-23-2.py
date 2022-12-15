# 傳遞任意數量的參數 
def make_icecream(*toppings):
    # 列出製作冰淇淋的配料
    print("這個所加配料如下")
    for topping in toppings:
        print("---", topping)
    print(type(toppings))
    print(toppings)


make_icecream()