# 地球到月球時間計算 重新設計ch3_25.py
dist = 384400  # 地球到月亮的距離
speed = 1225  # 馬赫速度每小時1225公里
sec_speed = speed / (60 * 60)  # 每秒鐘幾公里
total_seconds = dist // sec_speed
total_minutes, seconds = divmod(total_seconds, 60)
total_hours, minutes = divmod(total_minutes, 60)
days, hours = divmod(total_hours, 24)
print('需%d天%d小時%d分鐘%d秒' % (days, hours, minutes, seconds))
