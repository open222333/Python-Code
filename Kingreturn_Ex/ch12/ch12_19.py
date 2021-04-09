# 多重繼承
class Grandfather():
    """定義祖父類別"""

    def action1(self):
        print('Grandfather')


class Father(Grandfather):
    """定義父親類別"""

    def action3(self):  # 定義action3()
        print('Father')


class Uncle(Grandfather):
    """定義叔父類別"""

    def action2(self):  # 定義action2()
        print('Uncle')


class Ivan(Father, Uncle):
    """定義Ivan類別"""

    def action4(self):
        print('Ivan')


ivan = Ivan()
ivan.action4()  # 順序Ivan
ivan.action3()  # 順序Ivan -> Father
ivan.action2()  # 順序Ivan -> Father -> Uncle
ivan.action1()  # 順序Ivan -> Father -> Uncle -> Grandfather
