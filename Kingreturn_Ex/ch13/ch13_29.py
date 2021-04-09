# iskeyword() 檢查串列的字是否是關鍵字
import keyword  # 導入keyword模組

keywordList = ['as', 'while', 'break', 'sse', 'Python']
for x in keywordList:
    print("%8s " % x, keyword.iskeyword(x))
