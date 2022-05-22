from operator import le


def selection_sort(nLst):
    '''選擇排序'''
    for i in range(len(nLst) - 1):
        index = i  # 最小值的索引
        for j in range(i + 1, len(nLst)):  # 找最小值的索引
            if nLst[index][2] < nLst[j][2]:
                index = j
        if i == index:  # 如果目前索引是最小值索引
            pass
        else:
            nLst[i], nLst[index] = nLst[index], nLst[i]  # 資料對調
    return nLst


music = [
    ('A', 'SongA', 24740000),
    ('B', 'SongB', 8310000),
    ('C', 'SongC', 34130000),
    ('D', 'SongD', 12710000)
]

print('YouTube排行')
selection_sort(music)
for i in range(len(music)):
    print(f'{i + 1}:{music[i][0]}{music[i][1]} -- 點播次數{music[i][2]}')
