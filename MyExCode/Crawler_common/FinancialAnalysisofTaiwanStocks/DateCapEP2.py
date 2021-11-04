# 建立資料庫儲存資料
import pandas as pd
import sqlite3
import glob
import os

# 將工作目錄轉到此資料夾
os.chdir(os.path.dirname(os.path.abspath(__file__)))
# 將csv副檔名的檔案儲存在All_csv_file，glob用來查找特定檔案
All_csv_file = glob.glob('*.csv')
# dates_list 將日期檔名儲存為串列
dates_list = [file_name.replace('.csv', '') for file_name in All_csv_file]

# 以時間為表單存儲資料庫
dbname_1 = 'TWStock_1.db'
db = sqlite3.connect(dbname_1)
# 將讀取的資料存入資料庫
for file_name in All_csv_file:
    # 讀取抓到的資料，if_exisits='replace':
    pd.read_csv(file_name).iloc[:, 1:].to_sql(
        file_name.replace('.csv', ''), db, if_exists='replace')
# # 如何讀取資料庫的表格
# head()：顯示前幾筆資料 預設為5
# pd.read_sql(con=db,sql='SELECT * FROM "' + dates_list[0] + '"').head()

# 以公司為表單存儲成資料庫
total_df = pd.DataFrame()  # 建立一個表格
# 將所有csv資料存入total_df表格
for date in dates_list:
    # 依照日期選取資料
    df = pd.read_sql(con=db, sql='SELECT * FROM "' + date + '"')
    df['Date'] = date  # 增加一個新的欄位Date 內容為日期檔名串列的元素
    total_df = total_df.append(df)

total_df.shape  # 查看有多少(row,columns)列 行

dbname_2 = 'TWStock_2.db'
db2 = sqlite3.connect(dbname_2)

# 建立字典 groupby()：依照參數內進行分組
total_dict = dict(tuple(total_df.groupby('證券代號')))
# 將資料存入TWStock_2.db
for key in total_dict.keys():
    df = total_dict[key].iloc[:, 2:]
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values(by=['Date'])
    df.to_sql(key, db2, if_exists='replace')
# 讀取資料庫
# tail()：顯示後幾筆資料 預設為5
test = pd.read_sql(con=db2, sql='SELECT * FROM "2330"').tail()
