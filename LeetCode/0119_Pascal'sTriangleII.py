class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        ans = [[1]]
        for i in range(1, rowIndex + 1):
            row = [ans[i - 1][j - 1] + ans[i - 1][j] for j in range(1, i)]
            row.insert(0, 1)
            row.insert(i, 1)
            ans.append(row)
        return ans[rowIndex]


class Solution2:
    def getRow(self, rowIndex: int) -> list[int]:
        arr = [[1],[1,1]]
        for i in range(1, rowIndex):
            ans = [1]
            for j in range(len(arr[i - 1])):
                ans.append(arr[i][j] + arr[i][j + 1])
            ans.append(1)
            arr.append(ans)
        return arr[rowIndex]



print(Solution2().getRow(4))
