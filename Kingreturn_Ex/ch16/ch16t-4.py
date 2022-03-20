import re
import os
from typing import MutableSequence

dir_list = os.listdir('ch14')
filename_string = ''
for filename in dir_list:
    filename_string += (filename + ' ')
# 列印副檔名為txt的檔案
pattern = r'[A-Za-z0-9_]+.txt'
txts = re.findall(pattern, filename_string)
count = 0
for txt in txts:
    count += 1
    if count < len(txts):
        print(txt, end=', ')
    else:
        print(txt)
# 列印ch14_10.py~ch14_19.py
print("--------------------------")
pattern = r'ch14_1+[0-9]+.py'
txts = re.findall(pattern, filename_string)
for txt in txts:
    print(txt)
