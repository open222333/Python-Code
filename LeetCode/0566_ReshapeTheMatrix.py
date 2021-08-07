class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        '''自己的解法'''
        ans = []
        stock = []
        for ma in mat:
            for m in ma:
                stock.append(m)
        if len(stock) != r * c:
            return mat
        else:
            if len(stock) % c != 0:
                row = (len(stock) // c) + 1
            else:
                row = len(stock) // c
            for i in range(row):
                temp = []
                for j in range(i * c, (i + 1) * c):
                    temp.append(stock[j])
                ans.append(temp)
        return ans


mat = [[1, 2], [3, 4]]
r = 2
c = 2
print(Solution().matrixReshape(mat, r, c))
