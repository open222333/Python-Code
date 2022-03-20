# 影像的翻轉
from PIL import Image

pict = Image.open("ch17/out17_7.jpg")  # 建立Pillow物件
pict.transpose(Image.FLIP_LEFT_RIGHT).save("ch17/out17_12_1.jpg")  # 左右
pict.transpose(Image.FLIP_TOP_BOTTOM).save("ch17/out17_12_2.jpg")  # 上下
