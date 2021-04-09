# issubset() 可以測試一個集合是否為另一個集合的子集合
A = {'a', 'b', 'c'}
B = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'k'}
C = {'k', 'm', 'n'}
# 測試A和B集合
boolean = A.issubset(B)  # 所有A的元素皆是B的元素
print("A集合是B集合的子集合傳回值是 ", boolean)

# 測試C和B集合
boolean = C.issubset(B)  # 有共同的元素k
print("C集合是B集合的子集合傳回值是", boolean)
