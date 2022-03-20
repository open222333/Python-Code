# 衍生類別繼承基底類別的實例應用
class Father():
    def hometown(self):
        print('我住在台北')


class Son(Father):
    pass


hung = Father()
ivan = Son()
hung.hometown()
ivan.hometown()
