tp = (1, 2, 3, 4, 5, 2, 3, 1, 4)
tp_list = list(tp)
new_tplist = []
for i in tp_list:
    if i in new_tplist:
        continue
    else:
        new_tplist.append(i)
newtp = tuple(new_tplist)
print(newtp)
