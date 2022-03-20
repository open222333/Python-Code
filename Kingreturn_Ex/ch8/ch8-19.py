# 專題 認識元組
# 地球到月球時間計算
dist = 384400  # 地球到月亮的距離
speed = 1225  # 馬赫速度每小時1225公里
total_hours = dist // speed  # 計算小時數
data = divmod(total_hours, 24)  # 商和餘數
print("divmod傳回的料型態是：", type(data))
print("總共需要%d天" % data[0])
print("%d 小時" % data[1])
