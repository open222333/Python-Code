# symmetric_difference() 對稱對稱差集
A = {1, 2, 3, 4, 5}  # 定義集合A
B = {3, 4, 5, 6, 7}  # 定義集合B
# 將symmetric_difference()應用在A集合
AB = A.symmetric_difference(B)  # A和B的對稱差集
print("A和B的對稱差集是 ", AB)
# 將symmetric_difference()應用在B集合
BA = B.symmetric_difference(A)  # B和A的對稱差集
print("B和A的對稱差集是 ", BA)