# Approach 1: Two Pointers
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        length = 0
        if len(nums) == 0:
            return length
        for i in range(1, len(nums)):
            if nums[length] < nums[i]:
                length += 1
                nums[length] = nums[i]
        return length + 1

    def removeDuplicates2(self, nums: list[int]) -> int:
        # Two Pointers
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i + 1

    def removeDuplicates3(self, nums: list[int]) -> int:
        # Two Pointers
        slow, fast = 0, 1
        
        if len(nums) == 0 or len(nums) ==1:
            return len(nums)
        
        while fast < len(nums):      
		# fast pointer found distinct element so increment slow pointer and assign value which is at fast pointer.
            if nums[slow] < nums[fast]:
                slow += 1
                nums[slow]=nums[fast]
            fast += 1
        return slow+1 
                


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
nums.remove(nums[6])
print(nums)