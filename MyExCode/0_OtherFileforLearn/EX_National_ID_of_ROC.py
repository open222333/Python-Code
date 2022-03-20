# 猜 身分證字號
'''
https://zh.wikipedia.org/wiki/%E4%B8%AD%E8%8F%AF%E6%B0%91%E5%9C%8B%E5%9C%8B%E6%B0%91%E8%BA%AB%E5%88%86%E8%AD%89
'''


def mergeNumList(*args):
    # 合併
    return_list = []
    for i_list in args:
        for item in i_list:
            return_list.append(item)
    return_list.sort()
    return return_list


def verifyValidCode(IDCard: str):
    # 驗證 是否為有效碼
    IDnum = [s for s in IDCard]
    pass


# 性別
gender = {'male': '1', 'female': '2'}
# 地區
region = {
    'A': 10,  # 台北市
    'B': 11,  # 台中市
    'C': 12,  # 基隆市
    'D': 13,  # 台南市
    'E': 14,  # 高雄市
    'F': 15,  # 新北市
    'G': 16,  # 宜蘭縣
    'H': 17,  # 桃園市
    'I': 34,  # 嘉義市
    'J': 18,  # 新竹縣
    'K': 19,  # 苗栗縣
    'M': 21,  # 南投縣
    'N': 22,  # 彰化縣
    'O': 35,  # 新竹市
    'P': 23,  # 雲林縣
    'Q': 24,  # 嘉義縣
    'T': 27,  # 屏東縣
    'U': 28,  # 花蓮縣
    'V': 29,  # 台東縣
    'W': 32,  # 金門縣
    'X': 30,  # 澎湖縣
    'Z': 33,  # 連江縣
    'L': 20,  # 台中縣
    'R': 25,  # 台南縣
    'S': 26,  # 高雄縣
    'Y': 31,  # 陽明山管理局
}
# 動茲
dongzi_first_week = ['13', '19', '55', '71',
                     '93', '97', '381', '453', '644', '734', '985']
dongzi_second_week = ['91', '11', '04', '18', '57', '498', '756']
dongzi_third_week = ['82', '45', '57', '53',
                     '00', '546', '855', '865', '012', '983']
dongzi_fourth_week = ['30', '03', '51', '88']
dongzi = mergeNumList(dongzi_first_week, dongzi_second_week,
                      dongzi_third_week, dongzi_fourth_week)
# 國旅
guolu_first_week = ['21', '32', '98', '67', '97', '410']
guolu_second_week = ['87', '04', '40', '29', '71']
guolu_third_week = ['44', '34', '09', '55', '35', '041']
guolu_fourth_week = ['32', '02', '87', '93', '82', '17']
guolu = mergeNumList(guolu_first_week, guolu_second_week,
                     guolu_third_week, guolu_fourth_week)
# 農遊
nongyou_first_week = ['89', '32', '54', '597', '453', '152']
nongyou_second_week = ['50', '13']
nongyou_third_week = ['60', '75']
nongyou_fourth_week = ['315', '740', '381', '264',
                       '285', '765', '682', '763', '373', '015', '374']
nongyou = mergeNumList(nongyou_first_week, nongyou_second_week,
                       nongyou_third_week, nongyou_fourth_week)
