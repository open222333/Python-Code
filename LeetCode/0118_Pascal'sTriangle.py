class Solution:
    """自己的解法"""

    def generate(self, numRows: int) -> list[list[int]]:
        ans = [[1]]
        if numRows == 1:
            return ans
        else:
            for i in range(1, numRows):
                ans.append(self.rowlist(ans[i - 1]))
        return ans

    def rowlist(self, row: list[int]) -> list[int]:
        """傳回每一列的串列"""
        result = []
        result.append(1)
        for i in range(0, len(row) - 1):
            result.append(row[i] + row[i + 1])
        result.append(1)
        return result


class Solution2():
    def generate(self, numRows: int) -> list[list[int]]:
        ans = [[1]]
        for i in range(1, numRows):
            row = [ans[i - 1][j - 1] + ans[i - 1][j] for j in range(1, i)] # 上方rowlist
            row.insert(0, 1)
            row.insert(i, 1)
            ans.append(row)
        return ans


numRows = 5
print(Solution2().generate(numRows))
