def lenghtCheck(fn):
    try:
        with open(fn) as file_Obj:
            data = file_Obj.read()
    except FileNotFoundError:
        return '找不到 %s 檔案' % fn

    dataList = data.split()
    if len(dataList) > 35:
        raise Exception('文章字數：%d 文章字數過長' % len(dataList))
    if len(dataList) < 10:
        raise Exception('文章字數：%d 文章字數過短' % len(dataList))
    return '文章字數：%d' % len(dataList)


fileList = ['d1.txt', 'd2.txt', 'd2_1.txt',
            'd3.txt', 'd4.txt', 'd5.txt', 'd6.txt']
for file in fileList:
    try:
        print(lenghtCheck(('ch15/' + file)))
    except Exception as err:
        print(str(err))
