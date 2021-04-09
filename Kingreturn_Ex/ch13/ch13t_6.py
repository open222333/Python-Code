# choice() 從串列中隨機傳回一個元素
import random

dice_dict = {}
for i in range(601):
    i = random.choice([1, 2, 3, 4, 5, 6])
    if i in dice_dict:
        dice_dict[i] += 1
    else:
        dice_dict[i] = 1

new_dice_dict = {}
for i in sorted(dice_dict.keys()):
    new_dice_dict[i] = dice_dict[i]
print(new_dice_dict)
