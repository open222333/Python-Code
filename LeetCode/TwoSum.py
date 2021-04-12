from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, val in enumerate(nums):
            diff = target - val
            if diff in nums:
                y = nums.index(diff)
                ans = list((y,i))
        return ans

class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]