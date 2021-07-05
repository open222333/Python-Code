# 若內容是0 複製並插入0
class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """自己的解法"""
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                arr.insert(i + 1, 0)
                arr.pop()
                i += 2
            else:
                i += 1


arr = [1, 0, 2, 3, 0, 4, 5, 0]
Solution().duplicateZeros(arr)
print(arr)
