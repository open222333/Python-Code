# rstrip() lstrip() strip() 刪除空白字元應用
string = input("請輸入英文名字：")
print("/%s/" % string)
string = input("請輸入英文名字：").strip()
print("/%s/" % string)
string = input("請輸入英文名字：").strip().title()
print("/%s/" % string)
