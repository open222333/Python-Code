# Kadane’s Algorithm — (Dynamic Programming)
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        curr = nums[0]
        maxs = nums[0]
        for i in range(1, len(nums)):
            # 比對 目前的值 到目前的值子陣列 取最大值
            curr = max(nums[i], curr + nums[i])
            maxs = max(maxs, curr)
        return maxs


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
test = Solution().maxSubArray(nums)
print(test)
