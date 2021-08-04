class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans = []
        for i in range(len(nums1)):
            for j in range(nums2.index(nums1[i]) + 1, len(nums2)):
                if nums2[j] > nums1[i]:
                    ans.append(nums2[j])
                    break
            else:
                ans.append(-1)
        return ans


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(Solution().nextGreaterElement(nums1, nums2))
