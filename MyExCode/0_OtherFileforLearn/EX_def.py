'''def 引數為func'''

def funca():
    print('a')


def funcb():
    print('b')


def test(func):
    func()


test(funca)