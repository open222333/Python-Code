from pprint import pprint
# 走迷宮與回朔演算法 擴充規模

# 迷宮地圖
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# 使用串列設計走迷宮的方向
directions = [
    lambda x, y:(x-1, y),  # 往上走
    lambda x, y:(x+1, y),  # 往下走
    lambda x, y:(x, y-1),  # 往左走
    lambda x, y:(x, y+1),  # 往右走
]


def maze_solve(x, y, goal_x, goal_y):
    ''' 解迷宮遊戲
    x, y 迷宮入口
    goal_x, goal_y 迷宮出口'''
    maze[x][y] = 2
    stack = []  # 建立路徑堆疊
    stack.append((x, y))  # 將路徑push入堆疊
    print('迷宮開始')
    while (len(stack) > 0):
        cur = stack[-1]  # 目前位置
        if cur[0] == goal_x and cur[1] == goal_y:
            print('抵達出口')
            return True  # 抵達出口返回True
        for dir in directions:  # 依上,下,左,右優先順序走此迷宮
            next = dir(cur[0], cur[1])
            if maze[next[0]][next[1]] == 0:  # 如果是通道 可以走
                stack.append(next)
                maze[next[0]][next[1]] = 2  # 用2標記走過的路
                break
        else:  # 如果進入死路 則回朔
            maze[cur[0]][cur[1]] = 3  # 標記死路
            stack.pop()  # 回朔
    else:
        print('沒有路徑')
        return False


maze_solve(1, 1, 8, 2)
pprint(maze)
