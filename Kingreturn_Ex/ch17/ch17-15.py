# 裁切影像
from PIL import Image

pict = Image.open("ch17/out17_14.jpg")  # 建立Pillow物件
cropPict = pict.crop((80, 30, 150, 100))  # 裁切區間
cropPict.save("ch17/out17_15.jpg")
