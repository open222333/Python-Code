import random
import string


def encrypt(text, encryptdict):
    cipher = []
    for i in text:
        v = encryptdict[i]
        cipher.append(v)
    return ''.join(cipher)


def decrypt(text, decryptdict):
    cipher = []
    for i in text:
        v = decryptdict[i]
        cipher.append(v)
    return ''.join(cipher)


fn = 'ch14/zenofPython.txt'
with open(fn) as file_Obj:
    data = file_Obj.read()

abc = string.printable[:-3]
abclist = list(abc)
random.shuffle(abclist)
abcstr = ''.join(abclist)

encrypt_dict = dict(zip(abcstr, abc))
decrypt_dict = dict(zip(abc, abcstr))
endata = encrypt(data, encrypt_dict)
dedata = decrypt(endata, decrypt_dict)
with open('ch14/ch14t_15/zenofPython_Encry.txt', 'w', encoding='utf-8') as file_Obj:
    file_Obj.write(endata)

with open('ch14/ch14t_15/zenofPython_Decry.txt', 'w', encoding='utf-8') as file_Obj:
    file_Obj.write(dedata)
