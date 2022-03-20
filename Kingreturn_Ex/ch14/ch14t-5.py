targetFile = input("請輸入要複製的檔案路徑：")
newFile = input("請輸入新的檔案名字：")
with open(targetFile, 'r') as file_Obj:
    tmp = file_Obj.read()
    with open(newFile, 'w') as file_Obj:
        data = file_Obj.write(tmp)
