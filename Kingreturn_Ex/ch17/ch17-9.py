# 影像的編輯
from PIL import Image

pict = Image.open("ch17/out17_7.jpg")  # 建立Pillow物件
width, height = pict.size
newPict1 = pict.resize((width*2, height))  # 寬度是2倍
newPict1.save("ch17/out17_9_1.jpg")
newPict2 = pict.resize((width, height*2))  # 高度是2倍
newPict2.save("ch17/out17_9_2.jpg")
