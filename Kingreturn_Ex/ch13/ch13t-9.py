import keyword

keywords = input("請輸入字串：")
if keyword.iskeyword(keywords) == True:
    print("%s是關鍵字" % keywords)
else:
    print("%s不是關鍵字" % keywords)
