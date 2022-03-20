str1 = 'Python 入門到高手之路'
str2 = '作者：洪錦魁'
str3 = '深石數位科技'
str4 = 'DeepStone Corporation'
str5 = 'Deep Learning'
strlist = [str1, str2, str3, str4, str5]


with open('ch14/ex14_6_1.txt', 'w', encoding='utf-8') as file_Obj:
    for i in strlist:
        i += '\n'
        file_Obj.write(i)

with open('ch14/ex14_6_2.txt', 'w', encoding='utf-8') as file_Obj:
    for i in strlist:
        file_Obj.write(i.rstrip())

with open('ch14/ex14_6_3.txt', 'w', encoding='utf-8') as file_Obj:
    for i in strlist:
        i += '  '
        file_Obj.write(i)
