# Given an array of integers arr, return true if and only if it is a valid mountain array.
# Approach 1: One Pass
class Solution(object):
    def validMountainArray(self, A):
        N = len(A)
        i = 0

        # walk up
        while i+1 < N and A[i] < A[i+1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == N-1:
            return False

        # walk down
        while i+1 < N and A[i] > A[i+1]:
            i += 1

        return i == N-1

class Solution1:
    def validMountainArray(self, arr: list[int]) -> bool:
        """自己的解法"""
        topP = arr.index(max(arr))
        if topP == 0 or topP == len(arr) - 1 or len(arr) < 3: # 排除小於三 更快
            return False
        for i in range(topP):
            if arr[i] >= arr[i + 1]:
                return False
        for j in range(topP, len(arr) - 1):
            if arr[j] <= arr[j + 1]:
                return False
        return True

    def validMountainArray2(self, arr: list[int]) -> bool:
        """更快"""
        pass


arr = [0, 3, 2, 1]
print(Solution1().validMountainArray(arr))
