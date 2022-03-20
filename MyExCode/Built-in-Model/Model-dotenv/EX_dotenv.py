import os
from dotenv import load_dotenv

'''設定環境變數'''

os.chdir(os.path.dirname(__file__))
# 讀取env檔
load_dotenv('EX_dotenv.env')


# 取出環境變數內容
r1 = os.getenv('TEST')
r2 = os.environ.get('TEST')
print(r1)
print(r2)
