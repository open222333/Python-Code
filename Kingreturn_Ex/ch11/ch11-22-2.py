# 傳遞串列的提醒
def insertChar(letter, myList=None):
    if myList == None:
        myList = []
    myList.append(letter)
    print(myList)


insertChar('x')
insertChar('y')
