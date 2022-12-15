# 地球到月球時間計算 使用divmod()函數重新設計ch3_24.py
dist = 384400  # 地球到月亮的距離
speed = 1225  # 馬赫速度每小時1225公里
total_hours = dist // speed  # 計算小時數
days, hours = divmod(total_hours, 24)  # 商和餘數
print("總共需要天數")
print(days)
print("小時數")
print(hours)
