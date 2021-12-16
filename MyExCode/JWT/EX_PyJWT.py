# pip install PyJWT
import jwt


def jwt_encode(content: dict, secret_key):
    return jwt.encode(payload=content, key=secret_key)


content = {
    "password": "test1111"
}
secret_key = 'secret_key'
encoded_jwt = jwt_encode(content, secret_key)
print(encoded_jwt)
