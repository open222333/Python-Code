class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1D = {}
        ans = []
        for i in nums1:
            if i not in nums1D:
                nums1D[i] = 1
            else:
                nums1D[i] += 1
        for num in nums2:
            if num in nums1D and nums1D[num] != 0:
                nums1D[num] -= 1
                ans.append(num)
        return ans


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(Solution().intersect(nums1, nums2))
