def CtoF(c):
    """攝氏溫度轉華氏溫度"""
    f = c * 9 / 5 + 32
    return f


def FtoC(f):
    """華氏溫度轉攝氏溫度"""
    c = (f - 32) * 5 / 9
    return c
