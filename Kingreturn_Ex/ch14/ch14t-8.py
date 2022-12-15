fn = 'ch14/ex14_6_1.txt'
with open(fn) as file_Obj:
    data = file_Obj.readlines()

for line in data:
    print(line)
