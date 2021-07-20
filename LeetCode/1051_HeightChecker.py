class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        sortlist = heights.copy()
        sortlist.sort()
        print(sortlist)
        print(heights)
        ans = 0
        for i in range(0, len(heights)):
            if sortlist[i] != heights[i]:
                ans += 1
        return ans

    def heightChecker2(self, heights: list[int]) -> int:
        sort_heights = sorted(heights)
        ans = 0
        for i in range(0, len(heights)):
            if sort_heights[i] != heights[i]:
                ans += 1
        return ans

    def heightChecker3(self, heights: list[int]) -> int:
        return sum(a != b for a, b in zip(heights, sorted(heights)))


heights = [5, 1, 2, 3, 4]
print(Solution().heightChecker3(heights))
