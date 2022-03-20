# intersection_update()
A = {'a', 'b', 'c', 'd'}
B = {'a', 'k', 'c'}
C = {'c', 'f', 'w'}
# A將是A和B的交集
ret_value = A.intersection_update(B)
print(ret_value)
print("A集合 ＝ ", A)
print("B集合 ＝ ", B)

# A將是A,B,C的交集
ret_value = A.intersection_update(B, C)
print("A集合 ＝ ", A)
print("B集合 ＝ ", B)
print("C集合 ＝ ", C)
