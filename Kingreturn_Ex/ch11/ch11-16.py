# 函數回傳字典資料
def build_vip(id, name):
    """建立VIP資料"""
    vip_dict = {'VIP_ID': id, 'Name': name}
    return vip_dict


member = build_vip('101', 'Nelson')
print(member)
