import qrcode

codeText = 'http://www.deepstone.com.tw'
img = qrcode.make(codeText)  # 建立QRcode物件
print("檔案格式", type(img))
img.save("ch17/out17_23.jpg")
