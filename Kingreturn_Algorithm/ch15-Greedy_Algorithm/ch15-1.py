# 貪婪演算法(Greedy Algorithm)
# 局部現況採取最好的選擇

def greedy(course):
    '''貪婪演算法(Greedy Algorithm)'''
    length = len(course)  # 課程數量
    course_list = []  # 儲存結果
    course_list.append(course[0])  # 第一節課
    course_end_time = course_list[0][1][1]  # 第一節課下課時間
    for i in range(1, length):
        if course[i][1][0] >= course_end_time:  # 上課時間晚於或等於
            course_list.append(course[i])  # 加入貪婪選擇
            course_end_time = course[i][1][1]  # 新的下課時間
    return course_list


course = {
    '化學': (12, 13),
    '英文': (9, 11),
    '數學': (8, 10),
    '計概': (10, 12),
    '物理': (11, 13),
}
cs = sorted(course.items(), key=lambda item: item[1][1])  # 課程的時間排序
print('所有課程依下課時間排序如下')
print('課程', '開始時間', '下課時間')
for i in range(len(cs)):
    print('{0}{1:7d}:00{2:8d}:00'.format(cs[i][0], cs[i][1][0], cs[i][1][1]))

s = greedy(cs)  # 呼叫貪婪選擇
print('貪婪選擇課程如下')
print('課程', '開始時間', '下課時間')
for i in range(len(s)):
    print('{0}{1:7d}:00{2:8d}:00'.format(s[i][0], s[i][1][0], s[i][1][1]))
