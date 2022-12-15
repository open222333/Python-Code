def wordNum(fn):
    try:
        with open(fn) as file_Obj:
            data = file_Obj.read()
    except FileNotFoundError:
        return '找不到%s檔案' % fn
    else:
        wordList = data.split()
        return len(wordList)


fileList = []
while True:
    fileName = input("請輸入檔案路徑(輸入q或Q離開)：")
    if fileName == 'q' or fileName == 'Q':
        break
    fileList.append(fileName)

for file in fileList:
    if type(wordNum(file)) == int:
        print("%s 檔案的單字數量： %d" % (file, wordNum(file)))
    else:
        print(wordNum(file))
