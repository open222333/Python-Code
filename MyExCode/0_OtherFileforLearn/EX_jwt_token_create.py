import jwt
'''JWT 的全名是 JSON Web Token，是一種基於 JSON 的開放標準(RFC 7519)，它定義了一種簡潔(compact)且自包含(self-contained)的方式，用於在雙方之間安全地將訊息作為 JSON 物件傳輸。'''

payload = {
    'id': '',
    'account': '',
    'password': '',
}

token = jwt.encode(payload, 'secret_key')
print(token)
