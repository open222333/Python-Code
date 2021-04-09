# 匿名函數應用在高階函數的參數
def mycar(cars, func):
    for car in cars:
        print(func(car))


def wdcar(carbrand):
    return "My dream car is " + carbrand.title()


dreamcars = ['porsche', 'rolls royce', 'maserati']
mycar(dreamcars, wdcar)
