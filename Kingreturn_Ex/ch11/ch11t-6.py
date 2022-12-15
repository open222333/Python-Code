# 簡單傳回字串資料
def guest_info(firstname, middlename, lastname, gender):
    """整合客戶名字資料"""
    if gender == "M":
        welcome = middlename + firstname + ' ' + lastname + '先生歡迎你'
    else:
        welcome = middlename + firstname + ' ' + lastname + '小姐歡迎你'
    return welcome


info1 = guest_info('Ivan', 'Carl', 'Hung', 'M')
info2 = guest_info('Mary', 'Ice', 'Hung', 'F')
print(info1)
print(info2)
