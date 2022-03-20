# format函數的應用 輸出對齊方式的應用
r = 5
pi = 3.14159
area = r ** 2 * pi
print("/半徑{0:3d}圓面積{1:10.2f}/".format(r, area))
print("/半徑{0:>3d}圓面積{1:>10.2f}/".format(r, area))
print("/半徑{0:<3d}圓面積{1:<10.2f}/".format(r, area))
print("/半徑{0:^3d}圓面積{1:^10.2f}/".format(r, area))
