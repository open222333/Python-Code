from PIL import Image
from PIL import ImageFilter

rushMore = Image.open("ch17/out17_14.jpg")  # 建立Pillow物件
filterPict = rushMore.filter(ImageFilter.BLUR)
filterPict.save("ch17/out17_19_BLUR.jpg")
filterPict = rushMore.filter(ImageFilter.CONTOUR)
filterPict.save("ch17/out17_19_CONTOUR.jpg")
filterPict = rushMore.filter(ImageFilter.EMBOSS)
filterPict.save("ch17/out17_19_EMBOSS.jpg")
filterPict = rushMore.filter(ImageFilter.FIND_EDGES)
filterPict.save("ch17/out17_19_FIND_EDGES.jpg")
