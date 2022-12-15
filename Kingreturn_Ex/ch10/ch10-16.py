# 對稱差集 symmetric difference
math = {'Kevin', 'Peter', 'Eric'}  # 設定參加數學夏令營成員
physics = {'Peter', 'Nelson', 'Tom'}  # 設定參加物理夏令營成員
math_sydi_physics = math ^ physics
print('沒有同時參加物理夏令營和數學夏令營的成員', math_sydi_physics)
