# 影像的基礎操作
from PIL import Image

rushMore = Image.open("ch14/01.png")  # 建立Pillow物件
print("列出物件型態：", type(rushMore))
width, height = rushMore.size  # 獲得影像寬度和高度
print("寬度 ＝ ", width)
print("高度 ＝ ", height)
