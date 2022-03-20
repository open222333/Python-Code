# sample(串列,數量) 隨機傳回'數量'的串列元素
import random  # 導入random模組

super_lotto_lottos = random.sample(range(1, 50), 6)  # 6組號碼
specialNum = random.sample(range(1, 9), 1)  # 特別號

print("第xxx期威力彩號碼：")
print("特別號：%d" % specialNum[0])
print("普通號：", end="")
count = len(super_lotto_lottos)
for super_lotto_lotto in sorted(super_lotto_lottos):  # 排序列印威力彩號碼
    print(super_lotto_lotto, end=" ")
