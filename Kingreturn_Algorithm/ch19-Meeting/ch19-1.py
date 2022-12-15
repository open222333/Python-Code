# 質數
def is_prime(num):
    '''測試num是否質數'''
    for n in range(2, num):
        if num % n == 0:
            return False
    return True
