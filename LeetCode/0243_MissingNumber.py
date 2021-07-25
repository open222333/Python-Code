class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        for i in range(len(nums) + 1):
            if i not in nums:
                return i

    def missingNumber2(self, nums: list[int]) -> int:
        i = 0
        while i in nums:
            i += 1
        return i

    def missingNumber3(self, nums: list[int]) -> int:
        # Approach #4 Gauss' Formula [Accepted]
        return sum([i for i in range(len(nums) + 1)]) - sum(nums)

    def missingNumber4(self, nums: list[int]) -> int:
        # Approach #1 Sorting [Accepted]
        nums.sort()
        if nums[0] != 0:
            return 0
        elif nums[-1] != len(nums):
            return len(nums)
        for i in range(1, len(nums)):
            expected_num = nums[i - 1] + 1
            if nums[i] != expected_num:
                return expected_num

    def missingNumber5(self, nums: list[int]) -> int:
        # Approach #2 HashSet [Accepted]
        num_set = set(nums)
        n = len(nums) + 1
        for i in range(n):
            if i not in num_set:
                return i

    def missingNumber6(self, nums: list[int]) -> int:
        # Approach #3 Bit Manipulation [Accepted]
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
