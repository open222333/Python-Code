import pyotp
import qrcode

baseSecret = pyotp.random_base32()  # 隨機產生共享的密鑰(secret)
hotp1 = pyotp.TOTP(baseSecret)

counter = 1
totp = pyotp.TOTP(baseSecret)
totp.now()
totp.verify('492039')  # 驗證 OTP
qr_uri = pyotp.totp.TOTP(baseSecret).provisioning_uri("test")
img = qrcode.make(qr_uri)  # 建立QRCode
img.get_image().save("test.png")  # 儲存
img.get_image().show()  # 顯示
