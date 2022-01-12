from base64 import urlsafe_b64encode, b64encode


'''二進位資料處理'''
username = 'username'
password = 'password'
auth = f'{username}:{password}'.encode()
print(auth)
auth1 = b'Basic ' + b64encode(auth)
auth2 = b'Basic ' + urlsafe_b64encode(auth)
print(auth1)
print(auth2)
