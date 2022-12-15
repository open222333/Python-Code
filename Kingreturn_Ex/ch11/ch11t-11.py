def make_pizza(size, *toppings):
    msg = 'size:%s寸 配料' % size
    for topping in toppings:
        msg += (',' + topping)
    return msg


print(make_pizza(7, 'a', 'g', 'h', 'f'))
