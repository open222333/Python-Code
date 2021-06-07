# Approach 1: Brute Force
# Approach 2: Two Pointer Approach
# area = length * min (height_a, height_b):高要取短的
class Solution:
    def maxArea(self, height) -> int:
        size = len(height)
        left, right = 0, size - 1
        max_width = size - 1
        area = 0
        for width in range(max_width, 0, -1):
            if height[left] < height[right]:
                area = max(area, width * (height[left]))
                left += 1
            else:
                area = max(area, width * height[right])
                right -= 1
        return area
