# Given an array nums of integers, return how many of them contain an even number of digits.
# even number : 偶數
# 回傳偶數位數的數量

class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        ans = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                ans += 1
        return ans


nums = [12, 345, 2, 6, 7896]
print(Solution().findNumbers(nums))
