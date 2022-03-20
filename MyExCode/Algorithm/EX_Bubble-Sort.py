# 泡沫排序法
def bubble_sort(iterable):
    new_list = list(iterable)  # 轉成串列
    list_len = len(new_list)  # 長度
    for i in range(list_len):
        for j in range(list_len - i - 1):
            if new_list[j] > new_list[j + 1]:
                new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]
    return new_list
