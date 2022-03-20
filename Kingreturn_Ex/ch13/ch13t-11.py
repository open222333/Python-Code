import string


def encrypt(text, encryDict):
    cipher = []
    for i in text:  # 執行每個字元加密
        v = encryDict[i]  # 加密
        cipher.append(v)  # 加密結果紀錄在串列
    return ''.join(cipher)  # 串列轉成字串


def decrypt(text, decryptDict):
    cipher = []
    for i in text:
        v = decryptDict[i]
        cipher.append(v)
    return ''.join(cipher)


abc = string.printable[:-5]  # 取消不可列印字元
subtext = abc[-3:] + abc[:-3]  # 加密字串
encrypt_dict = dict(zip(subtext, abc))
decrypt_dict = dict(zip(abc, subtext))  # 解密字典
print("列印編碼字典\n", encrypt_dict)
msg = 'If the implementation is easy to explain,it may be a good idea.'
ciphertext = encrypt(msg, encrypt_dict)
decrypt_text = decrypt(ciphertext, decrypt_dict)

print("原始字串 ", msg)
print("加密字串 ", ciphertext)
print("解密字串 ", decrypt_text)
