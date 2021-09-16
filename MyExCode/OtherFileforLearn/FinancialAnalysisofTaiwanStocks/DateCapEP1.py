# 以函數建立抓取動作
import requests
import pandas as pd
import io
import datetime
import time
import os


def crawler(data_time):
    '''從台灣證卷交易所取得台股日線資料，參數：輸入字串格式"yyyymmdd"的日期。ex.20210401'''
    page_url = 'https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + \
        data_time + '&type=ALLBUT0999'
    page = requests.get(page_url)
    # splitlines()：按照行('\r', '\r\n', \n')分隔，返回一個包含各行作為元素的列表，如果參數 keepends 為 False，不包含換行符，如果為 True，則保留換行符。
    use_text = page.text.splitlines()
    # 找出所需內容第一行的索引值
    for i, text in enumerate(use_text):
        if text == '"證券代號","證券名稱","成交股數","成交筆數","成交金額","開盤價","最高價","最低價","收盤價","漲跌(+/-)","漲跌價差","最後揭示買價","最後揭示買量","最後揭示賣價","最後揭示賣量","本益比",':
            title_point = i
            break
    # 使用索引值印出列表，text[:-1]取代掉最後的逗號加上一個換行符號，''.join將字串連起來，io.StringIO：轉成文字檔以方便read_csv讀取
    text_df = pd.read_csv(io.StringIO(
        ''.join([text[:-1] + '\n' for text in use_text[title_point:]])))
    # 將證卷代號的欄位內的 = " 用空白取代掉
    text_df['證券代號'] = text_df['證券代號'].apply(lambda x: x.replace('"', ''))
    text_df['證券代號'] = text_df['證券代號'].apply(lambda x: x.replace('=', ''))
    return text_df


def trans_date(date_time):
    '''將datetime格式轉成可輸入至crawler函式的字串，參數：輸入datetime格式的日期'''
    return ''.join(str(date_time).split(' ')[0].split('-'))


def parse_n_days(start_date, n):
    '''抓取多天資料，參數：開始時間start_date，往前抓取n天'''
    df_dict = {}  # 建立一個字典，存日期資料
    now_date = start_date
    for i in range(n):
        # datetime.timedelta：表示時間間隔，即兩個時間點之間的長度。
        now_date = now_date - datetime.timedelta(days=1)
        # 是否成功抓取
        try:
            df = crawler(trans_date(now_date))  # 抓取結果
            print('Sussessful:%s' % trans_date(now_date))
            df_dict.update({trans_date(now_date): df})  # 將結果存進字典
        except:
            print('Fail:%s' % trans_date(now_date))
        time.sleep(3)  # 避免被停止抓取 每3秒抓一次
    return df_dict


result_dict = parse_n_days(datetime.datetime.now(), 10)
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # 將目前資料夾當作工作目錄
# 將資料輸出成csv檔
for key in result_dict.keys():
    result_dict[key].to_csv(str(key) + '.csv')
