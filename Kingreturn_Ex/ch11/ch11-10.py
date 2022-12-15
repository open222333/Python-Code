# return
def greeting(name):
    """Python函數需傳遞名字name"""
    print("Hi ", name, " Good Moring!")
    return  # Python將自動傳回None


ret_value = greeting('Nelson')
print("greeting()傳回值 ＝ ", ret_value)
print(ret_value, "的type ＝ ", type(ret_value))
