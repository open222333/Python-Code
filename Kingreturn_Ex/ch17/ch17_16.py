# 複製影像
from PIL import Image

pict = Image.open("ch17/out17_14.jpg")  # 建立Pillow物件
copyPict = pict.copy()  # 複製
copyPict.save("ch17/out17_16.jpg")
