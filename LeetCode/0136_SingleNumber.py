# Approach 1: List operation
# Algorithm
# Iterate over all the elements in \text{nums}nums
# If some number in \text{nums}nums is new to array, append it
# If some number is already in the array, remove it

# Approach 2: Hash Table

# Approach 3: Math
# Concept
# 2 * (a + b + c) - (a + a + b + b + c) = c

# Approach 4: Bit Manipulation
# Concept

# If we take XOR of zero and some bit, it will return that bit
# a \oplus 0 = aa⊕0=a
# If we take XOR of two same bits, it will return 0
# a \oplus a = 0a⊕a=0
# a \oplus b \oplus a = (a \oplus a) \oplus b = 0 \oplus b = ba⊕b⊕a=(a⊕a)⊕b=0⊕b=b


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        # Approach 2: Hash Table
        hash_table = {}
        for num in nums:
            if num not in hash_table:
                hash_table[num] = 1
            else:
                hash_table[num] += 1
        for key in hash_table.keys():
            if hash_table[key] == 1:
                return key

    def singleNumber2(self, nums: list[int]) -> int:
        # Approach 3: Math
        return sum(set(nums)) * 2 - sum(nums)

nums = [4, 1, 2, 1, 2]
print(Solution().singleNumber2(nums))
