# 留下最後N個項目
# 在迭代(iteration) 或某種處理動作的過程中留下最近幾個項目的少量歷程紀錄(limited history)
from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


# 在一個檔案上的使用範例
if __name__ == '__main__':
    with open('somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)

# 