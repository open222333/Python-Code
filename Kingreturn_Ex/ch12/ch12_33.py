class City():
    def __init__(self, name) -> None:
        self.name = name

    def __eq__(self, city2):
        return self.name.upper() == city2.name.upper()


one = City("Taipei")
two = City("taipei")
three = City("myhome")
print(one == two)
print(one == three)
