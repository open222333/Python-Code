# 每個步驟可為 n-1 個元素 增加1  最少步驟使全部元素相等

class Solution:
    def minMoves(self, nums: list[int]) -> int:
        return sum(nums) - len(nums) * min(nums)
