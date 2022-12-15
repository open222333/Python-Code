# 加密字典
abc = 'abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ'
front3 = abc[:-3]
end23 = abc[-3:]
subtext = end23 + front3
encry_dict = dict(zip(subtext, abc))
print(encry_dict)
