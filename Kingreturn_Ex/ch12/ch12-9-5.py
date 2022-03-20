# 計算正方形的面積
class Square():
    def __init__(self, sideLen):
        self.__sideLen = sideLen

    @property
    def area(self):
        return self.__sideLen ** 2


obj = Square(10)
print(obj.area)
