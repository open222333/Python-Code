class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        nums = set(nums)
        nums = list(nums)
        if len(nums) < 3:
            return max(nums)
        count = 0
        while count < 2:
            nums.remove(max(nums))
            count += 1
        return max(nums)

    def thirdMax2(self, nums: list[int]) -> int:
        nums = set(nums)
        return sorted(nums)[-3] if len(nums) > 2 else max(nums)


nums = [2, 2, 3, 1]
print(Solution().thirdMax(nums))
