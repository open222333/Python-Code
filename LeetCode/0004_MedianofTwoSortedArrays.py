# Given two sorted arrays nums1 and nums2 of size m and n respectively,
# return the median of the two sorted arrays.
import bisect
# The overall run time complexity should be O(log (m+n)).

# This one is a bit of a hack, as bisect_left is intended for lists, but
#  apparently it's happy enough with something that behaves enough like a list
#  (supports __getitem__):


class Solution1:
    def findMedianSortedArrays(self, nums1, nums2):
        a, b = sorted((nums1, nums2), key=len)
        m, n = len(a), len(b)
        after = (m + n - 1) / 2

        class Range:
            def __getitem__(self, i):
                return after - i - 1 < 0 or a[i] >= b[after - i - 1]
        i = bisect.bisect_left(Range(), True, 0, m)
        nextfew = sorted(a[i:i + 2] + b[after - i: after - i + 2])
        return (nextfew[0] + nextfew[1 - (m + n) % 2]) / 2.0


class Solution2:  # with a self-made binary search
    def finMedianSortedArrays(self, nums1, nums2):
        a, b = sorted((nums1, nums2), key=len)
        m, n = len(a), len(b)
        after = (m + n - 1) / 2
        lo, hi = 0, m
        while lo < hi:
            i = (lo + hi) / 2
            if after - i - 1 < 0 or a[i] >= b[after - i - 1]:
                hi = i
            else:
                lo = i + 1
        i = lo
        nextfew = sorted(a[i:i + 2] + b[after - i: after - i + 2])
        return (nextfew[0] + nextfew[1 - (m + n) % 2]) / 2.0
