# 三代同堂的類別與取得基底類別的屬性super()
class Grandfather():
    """定義祖父的資產"""

    def __init__(self):
        self.grandfathermoney = 10000
        super().__init__()

    def get_info1(self):
        print("Grandfather's information")


class Grandmother():
    def __init__(self):
        self.grandmothermoney = 20000
        super().__init__()

    def get_info4(self):
        print("Grandmother's information")


class Father(Grandfather, Grandmother):  # 父類別是Grandfather
    """定義父親的資產"""

    def __init__(self):
        self.fathermoney = 8000
        super().__init__()

    def get_info2(self):
        print("Father's information")


class Ivan(Father):  # 父類別是Father
    """定義Ivan的資產"""

    def __init__(self):
        self.ivanmoney = 3000
        super().__init__()

    def get_info3(self):
        print("Ivan's information")

    def get_money(self):  # 取得資產明細
        print("\nIvan資產：", self.ivanmoney,
              "\n父親資產：", self.fathermoney,
              "\n祖父資產：", self.grandfathermoney,
              "\n祖母資產：", self.grandmothermoney)


ivan = Ivan()
ivan.get_info3()  # 從Ivan中獲的
ivan.get_info2()  # 流程Ivan -> Father
ivan.get_info1()  # 流程Ivan -> Father -> Grandfathre
ivan.get_money()  # 取得資產明細
