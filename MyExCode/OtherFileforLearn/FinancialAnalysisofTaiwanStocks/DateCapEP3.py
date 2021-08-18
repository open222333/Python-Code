# 使用matplotlib以及pands進行資料探索
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import os

# 將工作目錄改成目前資料夾
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 連線資料庫
db = sqlite3.connect('TWStock_2.db')
stock_dict = {}
stock_dict.update({'tsmc': pd.read_sql(con=db, sql="SELECT * FROM '2330'")})

# 畫圖之前先整理資料
for key in stock_dict.keys():
    df = stock_dict[key]
    df.index = pd.to_datetime(df['Date'])  # 將index改成時間
    df = df[['證券名稱', '收盤價']]
    df['收盤價'] = pd.to_numeric(df['收盤價'].apply(
        lambda x: x.replace(',', '')), errors='coerce')  # 轉換成浮點數
    df.columns = ['stock_code', 'close']
    stock_dict[key] = df

# 畫圖
fig, ax = plt.subplots(3, 2, figsize=(10, 10))
plt.subplots_adjust(hspace=0.8)
stock_dict['tsmc']['2021-04-01':].plot(ax=ax[0, 0])
ax[0, 0].set_title('TSMC')
fig.suptitle("TEST")
plt.show()
