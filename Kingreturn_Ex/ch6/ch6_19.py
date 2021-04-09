# 串列為空串列的判斷
cars = ['Toyota', 'Nissan', 'Honda']
print("cars串列長度是 ＝ %d" % len(cars))
if len(cars) != 0:
    del cars[0]
    print("刪除cars串列元素成功")
    print("cars串列長度是 ＝ %d" % len(cars))
else:
    print("cars串列沒有任何資料")
nums = []
print("nums串列長度是 ＝ %d" % len(nums))
if len(nums) != 0:
    del nums[0]
    print("刪除nums串列元素成功")
    print("nums串列長度是 ＝ %d" % len(nums))
else:
    print("nums串列沒有任何資料")
