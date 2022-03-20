# 輸入飛機速度(公尺/秒)，加速度(公尺/秒) 輸出所需跑道長度
speed = eval(input("請輸入飛機速度(公尺/秒)："))
acceleration = eval(input("請輸入飛機加速度："))
distance = (speed ** 2) / (2 * acceleration)
print("所需跑到距離：%4.2f" % distance)
