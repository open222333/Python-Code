# 關鍵字參數 參數名稱 = 值
def interest(interest_type, subject):
    """顯示興趣和主題"""
    print("我的興趣是 " + interest_type)
    print("在 " + interest_type + "中,最喜歡的是 " + subject)
    print()

interest(interest_type='旅遊',subject='敦煌') # 位置正確
interest(subject='敦煌',interest_type='旅遊')#位置更動
