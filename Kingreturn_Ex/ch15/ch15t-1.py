# 分析單一文件的字數
inputdata = input('請輸入文字：')
fn = 'ch15/in15_6.txt'  # 設定欲開啟的檔案
try:
    with open(fn, 'w') as file_Obj:
        file_Obj.write(inputdata)
    with open(fn) as file_Obj:
        data = file_Obj.read()
except FileNotFoundError:
    print("找不到%s檔案" % fn)
else:
    wordList = data.split()  # 將文章轉成字串
    print(fn, "文章的字數是", len(wordList))  # 列印文章字數
