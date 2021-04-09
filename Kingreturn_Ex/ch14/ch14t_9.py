fn = 'ch14/ex14_6_1.txt'
with open(fn) as file:
    data = file.readlines()
for line in data:
    print(line.rstrip())
