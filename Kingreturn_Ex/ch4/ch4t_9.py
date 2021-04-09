# 重新設計ch2t_5.py 
# 計算地球飛到月亮需多久
distance = 384400  # 地球到月亮的距離
roket_speed = eval(input("請輸入火箭速度(公里/分鐘)："))  # 火箭速度 公里/分鐘
need_time = distance / roket_speed
print('從地球飛到月亮需%.0f分鐘' % need_time)
