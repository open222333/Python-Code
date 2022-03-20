# qrcode內有圖案
import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=5, error_correction=qrcode.ERROR_CORRECT_M, box_size=10, border=4)
qr.add_data("明志科技大學")
img = qr.make_image(fill_color='blue')
width, height = img.size  # QR code 的寬與高
print(width,height)
with Image.open('ch17/out17_6.png') as obj:
    obj_width, obj_height = obj.size
    img.paste(obj, (obj_width//100, obj_height//100))
print(obj_width,obj_height)
img.save("ch17/out17_23_3.jpg")
