# issuperset() 測試一個集合是否是另一個集合的父集合
A = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'k'}
B = {'a', 'b', 'c'}
C = {'k', 'm', 'n'}
# 測試A和B集合
boolean = A.issuperset(B)  # 測試
print("A集合是B集合的父集合傳回值是 ", boolean)

# 測試C和B集合
boolean = A.issuperset(C)  # 測試
print("A集合是C集合的父集合傳回值是", boolean)
