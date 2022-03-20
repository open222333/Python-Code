from base64 import urlsafe_b64encode

'''
https://docs.python.org/zh-tw/3/library/stdtypes.html#bytes.maketrans
https://docs.python.org/zh-tw/3/library/binascii.html
'''


def get_proxy_auth(username: str, password: str) -> bytes:
    '''http 標頭 Proxy-Authenticate
    取得 proxy authenticate 內容'''
    auth = f"{username}:{password}".encode(encoding='ISO-8859-1')
    auth = b"Basic " + urlsafe_b64encode(auth)
    return auth
