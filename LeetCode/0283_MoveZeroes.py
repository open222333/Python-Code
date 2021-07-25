class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        自己的解法
        Do not return anything, modify nums in-place instead.
        """
        for num in nums:
            if num == 0:
                nums.remove(num)
                nums.append(num)
        return nums

    def moveZeroes2(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        notZeroCount = 0
        length = len(nums)
        for i in range(length):
            if nums[i] != 0:
                nums[notZeroCount] = nums[i]
                notZeroCount += 1
        if notZeroCount:
            for j in range(notZeroCount, length):
                nums[j] = 0
        return nums


nums = [0, 1, 0, 3, 12]
print(Solution().moveZeroes2(nums))
