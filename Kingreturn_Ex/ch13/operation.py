#ch13t_2.py所需模組
def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def dev(n1, n2):
    if n2 == 0:
        return '除數不能為0'
    else:
        return n1 / n2
