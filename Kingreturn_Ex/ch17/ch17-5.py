# 取得檔案格式
from PIL import Image

rushMore = Image.open("ch14/01.png")  # 建立Pillow物件
print("列出物件副檔名：", rushMore.format)
print("列出物件描述：", rushMore.format_description)
