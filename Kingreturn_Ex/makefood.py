# 建立函數內容的模組
def make_icecream(*toppings):
    # 列出製作冰淇淋的配料
    print("這個所加配料如下")
    for topping in toppings:
        print("---", topping)


def make_drink(size, drink):
    # 輸入飲料規格與種類，然後輸出飲料
    print("所點飲料如下")
    print("--- ", size.title())
    print("--- ", drink.title())
