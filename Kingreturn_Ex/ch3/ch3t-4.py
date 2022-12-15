# 地球飛到月亮 需多少天多少小時多少分鐘
dist = 384400  # 距離
speed = 250  # 公里/分鐘
total_minute = dist // speed
total_hours = total_minute // 60
minutes = total_minute % 60
hours = total_hours % 24
days = total_hours // 24
print('總共需%d天%d小時%d分鐘' % (days, hours, minutes))
