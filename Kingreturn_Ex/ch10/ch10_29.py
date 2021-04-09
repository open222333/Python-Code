# isdisjoint() 兩個集合沒有共同元素會傳回True
A = {'a', 'b', 'c'}
B = {'c', 'd', 'e'}
C = {'h', 'k', 'p'}
# 測試A和B集合
boolean = A.isdisjoint(B)  # 有共同的元素'c'
print("有共同的元素傳回值是 ", boolean)

# 測試A和C集合
boolean = A.isdisjoint(C)  # 沒有共同元素
print("沒有共同的元素傳回值是 ", boolean)
