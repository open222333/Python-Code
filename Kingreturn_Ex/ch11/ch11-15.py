# 參數預設值 預設為空字串並放置最右邊 可處理沒有參數值的問題
def guest_info(firstname, lastname, gender, middlename=''):
    """整合客戶資料"""
    if gender == "M":
        welcome = lastname + middlename + firstname + '先生歡迎你'
    else:
        welcome = lastname + middlename + firstname + '小姐歡迎你'
    return welcome


info1 = guest_info('濤', '劉', 'M')
info2 = guest_info('雨', '洪', 'F', '冰')
print(info1)
print(info2)
