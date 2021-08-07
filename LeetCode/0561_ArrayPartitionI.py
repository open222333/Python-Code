class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        # 自己的解法
        nums.sort()
        ans = 0
        for i in range(0, len(nums), 2):
            ans += min(nums[i], nums[i + 1])
        return ans

    def arrayPairSum2(self, nums: list[int]) -> int:
        return sum(sorted(nums)[::2])


nums = [6, 2, 6, 5, 1, 2]
print(Solution().arrayPairSum(nums))
