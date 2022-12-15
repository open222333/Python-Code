import time


def lengthCheck(fn):
    try:
        with open(fn) as file_Obj:
            data = file_Obj.read()
    except FileNotFoundError:
        raise Exception('找不到%s檔案' % fn)
    else:
        dataList = data.split()
        if len(dataList) > 35:
            raise Exception('文章字數：%d,文章長度過長' % len(dataList))
        elif len(dataList) < 10:
            raise Exception('文章字數：%d,文章字數過短' % len(dataList))
        else:
            return '文章字數：%d' % len(dataList)


fileList = ['d1.txt', 'd2.txt', 'd2_1.txt',
            'd3.txt', 'd4.txt', 'd5.txt', 'd6.txt']
for file in fileList:
    try:
        print(lengthCheck('ch15/' + file))
    except Exception as err:
        with open('ch15/errdata.txt', 'a') as file_Obj:
            file_Obj.write("%s : %s \n" % (time.asctime(), str(err)))
        print(time.asctime() + ' : ' + str(err))
