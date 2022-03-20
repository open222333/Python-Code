from django.db import models
from django.contrib.auth.hashers import make_password
from django.utils import timezone
import pyotp
import qrcode
import uuid


class User(models.Model):
    account = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    accountID = models.UUIDField(default=uuid.uuid4)
    accountStateChoice = [
        ('Active', '正常'),
        ('Locked', '鎖定')
    ]
    accountState = models.CharField(
        max_length=10,
        choices=accountStateChoice,
        default='Active'
    )
    createDate = models.DateTimeField()
    lastEditDate = models.DateTimeField()
    googleSecret = models.CharField(max_length=50)
    googleQRCodeURL = models.TextField()
    loginStatusChoice = [
        ('online', '登入中'),
        ('offline', '未登入')
    ]
    loginStatus = models.CharField(
        max_length=10, choices=loginStatusChoice, default='offline')
    detial = models.TextField()

    def createUser(self, account, password):
        """創建帳號"""
        secret = pyotp.random_base32()
        imgQRCode = qrcode.make(pyotp.totp.TOTP(
            secret).provisioning_uri(account))
        imgQRCode.get_image().save(f"media/googleQRCode/{account}.png")
        addTemp = User(
            account=account,
            password=make_password(password),
            accountState='Active',
            createDate=timezone.now(),
            lastEditDate=timezone.now(),
            googleSecret=secret,
            googleQRCodeURL=f"media/googleQRCode/{account}.png",
            loginStatus='offline',
        )
        addTemp.save()

    def setRootAccount(self):
        """第一次開啟使用 建立root帳號"""
        if User.objects.filter(account="root").exists():
            pass
        else:
            User().createUser("root", "1qaz2wsx")

    def isLoggedIn(self, account):
        """判斷是否登入狀態"""
        accountData = User.objects.filter(account=account).get()
        if accountData.loginStatus == 'online':
            return True
        else:
            return False


class UserRecord(models.Model):
    recordID = models.UUIDField(primary_key=True)
    account = models.CharField(max_length=20)
    signInDataTime = models.DateTimeField()
    logOutDataTime = models.DateTimeField()

    def setSignInRecord(self, account):
        """創建登入紀錄"""
        addTemp = UserRecord(
            recordID=uuid.uuid1,
            account=account,
            signInDataTime=timezone.now(),
        )
        addTemp.save()

    def setLogOutRecord(self, account):
        """創建登出紀錄"""
        addTemp = UserRecord(
            account=account,
            logOutDataTime=timezone.now(),
        )
        addTemp.save()
