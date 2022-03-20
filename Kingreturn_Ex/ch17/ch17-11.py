from PIL import Image

pict = Image.open("ch17/out17_7.jpg")  # 建立Pillow物件
pict.rotate(45).save("ch17/out17_11_1.jpg")  # 旋轉45度
pict.rotate(45, expand=True).save("ch17/out17_11_2.jpg")  # 旋轉45度圖像擴充
