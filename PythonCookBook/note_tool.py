import re
import os

message = '問題：\n\n```\n```\n\n解法：\n\n```\n```\n\n討論：\n\n```\n```'
with open('PythonCookBook/test_title.txt', 'r') as f:
    content = f.readlines()
    for line in content:
        ch = re.findall(r'(.*?)\.', line)[0]
        dir_name = f"ch{ch}-"
        
        ignore_ch = ['1', '2'] # 已建立的章節
        if ch not in ignore_ch:
            # 判斷 Ch** 是否存在
            files = os.listdir('PythonCookBook')
            for file in files:
                if re.match(r'{}'.format(dir_name), file):
                    break
            else:
                os.makedirs(f"PythonCookBook/{dir_name}")
                
            with open(f'PythonCookBook/{dir_name}/ch{ch}-0-detial.md', 'a') as o:
                o.write(f"## {line}\n{message}\n\n")
            