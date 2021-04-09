# 影像合成
from PIL import Image
pict = Image.open("ch17/out17_14.jpg")  # 建立Pillow物件
copyPict = pict.copy()  # 複製
cropPict = copyPict.crop((80, 30, 150, 100))  # 裁切區間
copyPict.paste(cropPict, (20, 20))  # 第一次合成
copyPict.paste(cropPict, (20, 100))  # 第二次合成
copyPict.save("ch17/out17_17.jpg")  # 儲存
