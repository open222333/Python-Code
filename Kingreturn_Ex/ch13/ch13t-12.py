import string
import random


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


msg = 'If the implementation is easy to explain,it may be a good idea.'
abc = string.printable[:-5]
keydict = abc[:]
keydictlist = list(keydict)
random.shuffle(keydictlist)
keydictstr = ''.join(keydictlist)
encryptdict = dict(zip(keydictstr, abc))
decryptdict = dict(zip(abc, keydictstr))
encryptmsg = encrypt(msg, encryptdict)
decryptmsg = decrypt(encryptmsg, decryptdict)
print("加密字典 ", encryptdict)
print("解密字典 ", decryptdict)
print("原始字串 ", msg)
print("加密字串 ", encryptmsg)
print("解密字串 ", decryptmsg)
