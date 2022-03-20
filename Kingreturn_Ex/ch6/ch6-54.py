# is 和 is not 運算式 應用在整數變數
x = 10
y = 10
z = 15
r = z - 5
boolean_value = x is y
print("x位址 = %d,y位址 = %d" % (id(x), id(y)))
print("x = %d, y = %d" % (x, y),boolean_value)

boolean_value = x is z
print("x位址 = %d,z位址 = %d" % (id(x), id(z)))
print("x = %d, z = %d" % (x, z),boolean_value)

boolean_value = x is r
print("x位址 = %d,r位址 = %d" % (id(x), id(r)))
print("x = %d, r = %d" % (x, r),boolean_value)

boolean_value = x is not y
print("x位址 = %d,y位址 = %d" % (id(x), id(y)))
print("x = %d, y = %d" % (x, y),boolean_value)

boolean_value = x is not z
print("x位址 = %d,z位址 = %d" % (id(x), id(z)))
print("x = %d, z = %d" % (x, z),boolean_value)

boolean_value = x is not r
print("x位址 = %d,r位址 = %d" % (id(x), id(r)))
print("x = %d, r = %d" % (x, r),boolean_value)
