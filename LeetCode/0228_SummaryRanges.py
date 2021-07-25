class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        # Runtime: 24 ms, faster than 95.11% of Python3 online submissions for Summary Ranges.
        # Memory Usage: 14.3 MB, less than 48.45% of Python3 online submissions for Summary Ranges.
        stock = []
        temp = []
        ans = []
        if len(nums) == 0:
            return ans
        
        temp.append(nums[0])
        for i in range(1, len(nums)):
            if nums[i] - 1 == nums[i - 1]:
                temp.append(nums[i])
            else:
                stock.append(temp)
                temp = []
                temp.append(nums[i])
        stock.append(temp)
        for j in stock:
            if len(j) == 1:
                ans.append(f"{j[0]}")
            else:
                ans.append(f"{j[0]}->{j[len(j) - 1]}")
        return ans


nums = [0, 2, 3, 4, 6, 8, 9]
# nums = []
# nums = [-1]
print(Solution().summaryRanges(nums))
