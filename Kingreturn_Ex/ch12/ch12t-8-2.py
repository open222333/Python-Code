# 多重繼承
class Grandfather():
    """定義祖父類別"""

    def action1(self):
        print('Grandfather')


class Father(Grandfather):
    """定義父親類別"""

    def action2(self):  # 定義action2()
        print('Father')


class Uncle(Grandfather):
    """定義叔父類別"""

    def action2(self):  # 定義action2()
        print('Uncle')


class Aunt(Grandfather):
    def action2(self):
        print('Aunt')


class Ivan(Uncle, Aunt, Father):
    """定義Ivan類別"""

    def action3(self):
        print('Ivan')


ivan = Ivan()
ivan.action3()  # 順序Ivan
ivan.action2()  # 順序Ivan -> Father
ivan.action1()  # 順序Ivan -> Father -> Grandfather
