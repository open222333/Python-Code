class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        perimeter = 0
        for row_index, row in enumerate(grid):
            # grid[row_index][col_index]
            for col_index, land in enumerate(row):
                print(f'[{row_index}][{col_index}]={grid[row_index][col_index]}')
                if not land:
                    continue
                perimeter += 4
                # 垂直
                if col_index and row[col_index - 1]:
                    perimeter -= 2
                # 水平
                if row_index and grid[row_index - 1][col_index]:
                    perimeter -= 2
        return perimeter


grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
print(Solution().islandPerimeter(grid))
