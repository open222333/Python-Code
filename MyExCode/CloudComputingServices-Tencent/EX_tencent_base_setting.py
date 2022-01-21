import logging
import os
import sys
import dotenv

# 騰訊雲模組
from qcloud_cos import CosConfig, CosS3Client

'''測試 騰訊雲SDK 對象儲存'''

# 指定當前位置為工作目錄 讀取env檔
os.chdir(os.path.abspath(os.path.dirname(__file__)))
env = dotenv.dotenv_values("test_config.env")

# 日誌設定
# 正常情形，別使用INFO
# 需定位可使用DEBUG，此時SDK會印出與伺服器端的通信訊息
logging.basicConfig(level=logging.INFO, stream=sys.stdout)

# 設置用戶屬性
config = CosConfig(
    Region=env['TENCENT_BUCKET_REGION'],  # 地區
    SecretId=env['TENCENT_SECRET_ID'],
    SecretKey=env['TENCENT_SECRET_KEY'],

    # Token若用永久密鑰可不填 以下網址為 臨時密鑰生成與使用 指引
    # https://cloud.tencent.com/document/product/436/14048
    Token=None,
    Scheme='https'  # 指定用什麼協議訪問 預設https 可不填
)

# 連線
client = CosS3Client(config)
bucket_name = env['TENCENT_BUCKET_NAME']
