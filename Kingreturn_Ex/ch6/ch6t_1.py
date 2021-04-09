# 列出最高分 最低分 總分 平均
scorces = [87, 99, 69, 52, 78, 98, 80, 92]
print("分數為：", scorces, "\n最高分：%d,最低分：%d,總分：%d,平均：%d" %
      (max(scorces), min(scorces), sum(scorces), sum(scorces)/len(scorces)))
