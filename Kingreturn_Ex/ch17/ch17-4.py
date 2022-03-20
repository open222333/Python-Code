# 取得影像物件檔案的名稱
from PIL import Image

rushMore = Image.open("ch14/01.png")  # 建立Pillow物件
print("列出物件名稱：", rushMore.filename)
