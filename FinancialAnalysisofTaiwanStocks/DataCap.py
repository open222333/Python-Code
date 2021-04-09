# 在台灣證卷交易所爬蟲取的資料
import requests
import pandas as pd
import io

url = 'https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=20210408&type=ALLBUT0999'
page = requests.get(url)

use_text = pd.read_csv('file')