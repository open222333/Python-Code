# 重新設計 ch3_24.py
# 地球到月球時間計算
ma = eval(input("請輸入馬赫數："))
dist = 384400  # 地球到月亮的距離
speed = 1225 * ma  # 馬赫速度每小時1225公里
total_hours = dist // speed  # 計算小時數
days = total_hours // 24  # 商=計算天數
hours = total_hours % 24  # 餘數=計算小時數
print("總共需要%d天%d小時" % (days, hours))
