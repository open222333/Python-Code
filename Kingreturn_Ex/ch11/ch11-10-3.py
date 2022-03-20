# 空串列 空元組 空字典 空集合 布林值True與False和None之間的間隔
def is_None(string, x):
    if x is None:
        print("%s = None" % string)
    elif x:
        print("%s = True" % string)
    else:
        print("%s = False" % string)


is_None("空串列", [])  # 空串列
is_None("空元組", ())  # 空元組
is_None("空字典", {})  # 空字典
is_None("空集合", set())  # 空集合
is_None("None ", None)
is_None("True ", True)
is_None("False ", False)
