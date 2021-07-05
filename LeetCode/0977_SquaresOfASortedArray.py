# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
# non-decreasing : 不減
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        ans = []
        for num in nums:
            ans.append(num ** 2)
        ans.sort()
        return ans


nums = [-4, -1, 0, 3, 10]
print(Solution().sortedSquares(nums))
