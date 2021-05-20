'''
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.

一個整數數組，找出兩個數字，加起來等於目標數字，回傳數字在數組的位置
'''
from typing import List
# Approach 1: Brute Force
"""
Loop through each element x and find if there is another value that equals to target−x.
"""
# Approach 2: Two-pass Hash Table
# Approach 3: One-pass Hash Table


class Solution:
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, val in enumerate(nums):
            diff = target - val
            if diff in nums:
                y = nums.index(diff)  # 第二個數字的位置
                ans = list((y, i))
        return ans


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
