# 建立新的影像物件
from PIL import Image

pictObj = Image.new("RGB",(300,180),"aqua") #建立aqua顏色影像
pictObj.save("ch17/out17_7.jpg")