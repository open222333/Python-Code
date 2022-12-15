# 串列個數len()
james = [23, 19, 22, 31, 18]  # 定義james串列
games = len(james)  # 獲得場次數據
print("經過%d場比賽，最高得分：" % games, max(james))
print("經過%d場比賽，最低得分：" % games, min(james))
print("經過%d場比賽，得分統計：" % games, sum(james))
