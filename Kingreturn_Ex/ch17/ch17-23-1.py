import qrcode

codeText = 'Python王主歸來'
img = qrcode.make(codeText)  # 建立qrcode物件
print("檔案格式", type(img))
img.save("ch17/out17_23_1.jpg")
