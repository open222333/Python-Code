# Approach 1: Brute Force
# Approach 2: HashMap
# Approach 3: Sorting
# Approach 4: Randomization
from collections import Counter


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        hash_table = {}
        for num in nums:
            if num not in hash_table:
                hash_table[num] = 1
            else:
                hash_table[num] += 1
        return max(hash_table, key=hash_table.get)

    def majorityElement2(self, nums: list[int]) -> int:
        # Approach 2: HashMap
        count = Counter(nums)
        return max(count.keys(), key=count.get)

    def majorityElement3(self, nums: list[int]) -> int:
        # Approach 3: Sorting
        return sorted(nums)[len(nums) // 2]


nums = [2, 2, 1, 1, 1, 2, 2]
print(Solution().majorityElement3(nums))
