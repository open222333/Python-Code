# 衍生類別與基底類別有相同名稱的方法
class Person():
    def job(self):
        print("我是老師")


class LawerPerson(Person):
    def job(self):
        print("我是律師")


hung = Person()
ivan = LawerPerson()
hung.job()
ivan.job()
