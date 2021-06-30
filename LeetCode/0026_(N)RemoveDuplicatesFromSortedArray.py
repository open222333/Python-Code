# Approach 1: Two Pointers
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        stack = []
        result = []
        length = 0
        for num in nums:
            if num in result:
                stack.append("_")
            else:
                result.append(num)
                length += 1
        result.sort()
        result += stack
        return length, result

    def removeDuplicates2(self, nums: list[int]) -> int:
        length = 0
        if len(nums) == 0:
            return length
        for i in range(1,len(nums)):
            if nums[length] < nums[i]:
                length += 1
                nums[length] = nums[i]
        return length + 1

 
nums = [0,0,1,1,1,2,2,3,3,4]
test = Solution().removeDuplicates2(nums)
print(test, nums)