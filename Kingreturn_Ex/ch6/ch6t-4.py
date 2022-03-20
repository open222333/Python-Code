citys = ['Tokyo', 'City2', 'City3', 'City4', 'City5']
print('A', citys)
citys.append('London')  # 最後位置增加'London'
print('B', citys)
citys.insert(len(citys) // 2, 'Xian')  # 中央位置增加'Xian'
print('C', citys)
citys.remove('Tokyo')  # 使用remove()刪除'Tokyo'
print('D', citys)
