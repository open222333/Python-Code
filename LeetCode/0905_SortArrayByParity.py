# Approach 1: Sort
class Solution(object):
    def sortArrayByParity(self, A):
        A.sort(key=lambda x: x % 2)
        return A
# Approach 2: Two Pass


class Solution(object):
    def sortArrayByParity(self, A):
        return ([x for x in A if x % 2 == 0] +
                [x for x in A if x % 2 == 1])
# Approach 3: In-Place


class Solution(object):
    def sortArrayByParity(self, A):
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] % 2 > A[j] % 2:
                A[i], A[j] = A[j], A[i]

            if A[i] % 2 == 0:
                i += 1
            if A[j] % 2 == 1:
                j -= 1

        return A


class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        ans = []
        for num in nums:
            if num % 2 == 0:
                ans.append(num)
        for num in nums:
            if num not in ans:
                ans.append(num)
        return ans


nums = [3, 1, 2, 4]
