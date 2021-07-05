class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1 = nums1[:m]
        nums2 = nums2[:n]
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        return nums1

    def merge2(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for j in range(0, n):
            nums1[m + j] = nums2[j]
        nums1.sort()


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
print(Solution().merge2(nums1, m, nums2, n))
print(nums1)
