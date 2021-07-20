class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        setnums = set(nums)
        ans = []
        for i in range(len(nums)):
            if i + 1 not in setnums:
                ans.append(i + 1)
        return ans


# nums = [4, 3, 2, 7, 8, 2, 3, 1]
nums = [1, 1]
print(Solution().findDisappearedNumbers(nums))
