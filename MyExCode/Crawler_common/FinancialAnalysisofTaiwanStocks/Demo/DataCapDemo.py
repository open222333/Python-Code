# 在台灣證卷交易所爬蟲取的資料
import requests
import pandas as pd
import io

# 抓取網頁資料
url = 'https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=20210408&type=ALLBUT0999'
page = requests.get(url)

# 先行列印資料
use_text = page.text.splitlines()
# print(use_text)
# 將文字檔處理成pands可以處理的格式

# 使用for迴圈以及enumerate物件找到要抓取的標題位置的索引值
for i, text in enumerate(use_text):
    if text == '"證券代號","證券名稱","成交股數","成交筆數","成交金額","開盤價","最高價","最低價","收盤價","漲跌(+/-)","漲跌價差","最後揭示買價","最後揭示買量","最後揭示賣價","最後揭示賣量","本益比",':
        initital_point = i
        break

# 使用索引值印出列表，text[:-1]取代掉最後的逗號加上一個換行符號，''.join將字串連起來，io.StringIO：轉成文字檔以方便read_csv讀取
test_df = pd.read_csv(io.StringIO(
    ''.join([text[:-1] + '\n' for text in use_text[initital_point:]])))
# 將證卷代號的欄位內的 = " 用空白取代掉
test_df['證券代號'] = test_df['證券代號'].apply(lambda x: x.replace('"', ''))
test_df['證券代號'] = test_df['證券代號'].apply(lambda x: x.replace('=', ''))
