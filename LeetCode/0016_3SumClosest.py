# Approach 1: Two Pointers
class Solution1:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        diff = float("inf")
        nums.sort()
        for i in range(len(nums)):
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                sum = nums[i] + nums[lo] + nums[hi]
                if abs(target - sum) < abs(diff):
                    diff = target - sum
                if sum < target:
                    lo += 1
                else:
                    hi -= 1
            if diff == 0:
                break
        return target - diff


# Approach 2: Binary Search
class Solution2:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        pass
        # diff = float('inf')
        # nums.sort()
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         complement = target - nums[i] - nums[j]
        #         hi = bisect_right(nums, complement, j + 1)
        #         lo = hi - 1
        #         if hi < len(nums) and abs(complement - nums[hi]) < abs(diff):
        #             diff = complement - nums[hi]
        #         if lo > j and abs(complement - nums[lo]) < abs(diff):
        #             diff = complement - nums[lo]
        #     if diff == 0:
        #         break
        # return target - diff


# works for any k, not only for 3
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        return

    def KSumClosest(self, nums: list[int], k: int, target: int):
        N = len(nums)
        if N == k:
            return sum(nums[:k])

        # target too small
        current = sum(nums[:k])
        if current >= target:
            return current

        # target too big
        current = sum(nums[-k:])
        if current <= target:
            return current

        if k == 1:
            return min([(x, abs(target - x)) for x in nums], key=lambda x: x[1])[0]

        closest = sum(nums[:k])
        for i, x in enumerate(nums[:-k+1]):
            if i > 0 and x == nums[i-1]:
                continue
            current = self.KSumClosest(nums[i+1:], k-1, target - x) + x
            if abs(target - current) < abs(target - closest):
                if current == target:
                    return target
                else:
                    closest = current

        return closest
