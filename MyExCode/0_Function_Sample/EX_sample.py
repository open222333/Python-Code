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
