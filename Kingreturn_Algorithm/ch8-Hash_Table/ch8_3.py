# 雜湊表 選民名冊
def check_name(name):
    if voted[name]:
        print('你已經投過票了')
    else:
        print('歡迎投票')
        voted[name] = True


voted = {}  # 建立選民名單
voted = {'Trump': None, 'Lisa': None, 'Mike': None}
