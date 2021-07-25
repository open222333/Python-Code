class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        """Time Limit Exceeded"""
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    if abs(i - j) <= k:
                        return True
        else:
            return False

    def containsNearbyDuplicate2(self, nums: list[int], k: int) -> bool:
        d = {}
        for value, index in enumerate(nums):
            print(value, index)
            if d.get(index) and value + 1 - d[index] <= k:
                return True
            d[index] = value + 1
            print(d)
        return False

    def containsNearbyDuplicate3(self, nums: list[int], k: int) -> bool:
        if len(nums) == len(set(nums)):
            return False
        if len(nums) <= k + 1:
            return True
        duplicate = {}
        # dupes = []
        for i in range(len(nums)):
            if nums[i] in duplicate:
                duplicate[nums[i]].append(i)
            else:
                duplicate[nums[i]] = [i]
        for values in duplicate.values():
            if len(values) == 1:
                continue
            for i in range(len(values) - 1):
                if abs(values[i] - values[i + 1]) <= k:
                    return True
        return False


nums = [1, 2, 3, 1, 2, 3]
k = 2
# nums = [1, 0, 1, 1]
# k = 1
# nums = [1, 2, 3, 1]
# k = 3
print(Solution().containsNearbyDuplicate2(nums, k))
