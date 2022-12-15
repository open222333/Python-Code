def isTrangle(s1, s2, s3):
    """判斷三個邊長能否形成三角形"""
    if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
        return True
    else:
        return False


def area(s1, s2, s3):
    """使用三個邊長計算三角面積"""
    p = (s1 + s2 + s3) / 2
    area = (p * (p - s1) * (p - s2) * (p - s3)) ** 0.5
    return area


a, b, c = eval(input("請輸入三角形三個邊長(使用逗號分開)："))
if isTrangle(a, b, c) == True:
    print(area(a, b, c))
else:
    print("輸入邊長無法形成三角形")
