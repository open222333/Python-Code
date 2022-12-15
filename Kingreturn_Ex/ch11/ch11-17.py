# 函數傳回字典資料
def build_vip(id, name, tel=''):
    """建立VIP資訊"""
    vip_dict = {'VIP_ID': id, 'Name': name}
    if tel:
        vip_dict['Tel'] = tel
    return vip_dict


member1 = build_vip('101', 'Nelson')
member2 = build_vip('102', 'Henry', '0952222333')
print(member1)
print(member2)
