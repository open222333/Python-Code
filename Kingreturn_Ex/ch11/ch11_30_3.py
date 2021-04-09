# locals()：用字典列出所有的區域變數名稱與內容 globals()：用字典列出所有的全域變數名稱與內容
def printlocal():
    lang = "Java"
    print("語言：", lang)
    print("區域變數：", locals())


msg = "Python"
printlocal()
print("語言：", msg)
print("區域變數：", globals())
