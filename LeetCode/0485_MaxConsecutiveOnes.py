class Solution:
    """自己的解法"""
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        ans = 0
        temp = 0
        for i in nums:
            if i == 0:
                ans = max(ans, temp)
                temp = 0
            else:
                temp += 1
        ans = max(ans, temp)
        return ans

class Solution2():
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        pass


print(Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
