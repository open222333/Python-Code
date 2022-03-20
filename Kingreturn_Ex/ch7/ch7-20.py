# A * B = {(a , b)} 簡化
colors = ['Red', 'Green', 'Blue']
shapes = ['Circle', 'Square']
result = [[color, shape] for color in colors for shape in shapes]
for color, shape in result:
    print(color, shape)
