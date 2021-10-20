import jwt

payload = {
    'email':'test@ex.com',
    'name':'test'
}

token = jwt.encode(payload=payload, key='secret_key')
print(token)