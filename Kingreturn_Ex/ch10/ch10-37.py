# 專題 夏令營程式
# students是學生名單集合
students = {'Peter', 'Norton', 'Kevin', 'Mary',
            'Joho', 'Ford', 'Nelson', 'Damon', 'Ivan', 'Tom'}
Math = {'Peter', 'Kevin', 'Damon'}  # 數學夏令營參加人員
Physics = {'Nelson', 'Damon', 'Tom'}  # 物理夏令營參加人員
MandP = Math | Physics
print("有%d人參加數學和物理夏令營名單：" % len(MandP), MandP)
unAttend = students - MandP
print("沒有參加任何夏令營有%d人 名單是：" % len(unAttend), unAttend)
