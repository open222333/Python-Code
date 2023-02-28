import os
import re
from datetime import datetime

os.chdir(os.path.dirname(__file__))
with open('input.txt', 'r') as f:
    all_msgs = f.readlines()


amount = 0
with open(f'output-{datetime.now().__format__("%Y%m%d")}.txt', 'a') as f:
    for msg in all_msgs:
        match_msg = re.search(r'(?P<account>.*)的大頭貼照', msg)
        if match_msg:
            amount += 1
            f.write(f"{match_msg.group('account')}\n")
        else:
            print(msg)
