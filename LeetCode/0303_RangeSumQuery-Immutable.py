# Approach #1 (Brute Force) [Time Limit Exceeded]
# Approach #2 (Caching) [Accepted]
class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum([self.nums[i] for i in range(left, right + 1)])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
class NumArray2:
    # Runtime: 6628 ms, faster than 11.36% of Python3 online submissions for Range Sum Query - Immutable.
    # Memory Usage: 17.4 MB, less than 91.77% of Python3 online submissions for Range Sum Query - Immutable.
    # Brute Force
    def __init__(self, nums: list[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        ans = 0
        for i in range(left, right + 1):
            ans += self.nums[i]
        return ans


class NumArray3:
    # Caching
    def __init__(self, nums: list[int]):
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.nums[right]
        else:
            return (self.nums[right] - self.nums[left - 1])
