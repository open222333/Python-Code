import sys


'''Command Line Arguments 命令列參數'''
# 所有參數的數量
# agrs_num = len(sys.argv)
sum_result = 0

for i in sys.argv[1:]:
    sum_result += int(i)

print(sum_result)
