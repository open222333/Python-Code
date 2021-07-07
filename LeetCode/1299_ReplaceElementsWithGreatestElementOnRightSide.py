# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.
import itertools


class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        """自己的解法"""
        for i in range(len(arr) - 1):
            arr[i] = max(arr[i + 1:len(arr)])
        arr[len(arr) - 1] = -1

    def replaceElements2(self, arr: list[int]) -> list[int]:
        return list(itertools.accumulate(reversed(arr[1:]), func=max, initial=1))[::-1]


arr = [17, 18, 5, 4, 6, 1]
arr2 = [400]
# Solution().replaceElements(arr2)
# print(arr2)
print(Solution().replaceElements2(arr))
