import typing


def get_kwargs(**kwargs: list):
    '''**kwargs 應用'''
    '''
    get_kwargs(title=['tes1', 'test2', 'test3'])
    get_kwargs(title='test')
    '''
    for key, value in kwargs.items():
        print(f'key:{key}, all_values:{value}')
        if isinstance(value, list):
            for i in value:
                print(f'value: {i}')
        else:
            print(f'value: {value}')


def get_item(item: typing.Any = None):
    '''引數強制狀態以及設定預設'''
    print(item)


'''def 引數為func'''

def funca():
    print('a')


def funcb():
    print('b')


def test(func):
    func()


test(funca)
