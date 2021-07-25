# Approach #1 (Naive Linear Search) [Time Limit Exceeded]
# Approach #2 (Sorting) [Accepted]
# Approach #3 (Hash Table) [Accepted]

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # if len(nums) == len(set(nums)):
        #     return False
        # else:
        #     return True
        return len(nums) != len(set(nums))
