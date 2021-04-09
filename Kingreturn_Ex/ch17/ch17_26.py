# 繁體中文圖片
from PIL import Image
import pytesseract

text = pytesseract.image_to_string(
    Image.open("ch17/testch.png"), lang='chi_tra')
print(text)
with open("ch17/out17_26.txt", 'w') as fn:
    fn.write(text)
