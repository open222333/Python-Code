class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        if len(s) == 0:
            return 0
        gd = {}
        sd = {}
        ans = 0
        for i in g:
            if i not in gd:
                gd[i] = 1
            else:
                gd[i] += 1
        for j in s:
            if j not in sd:
                sd[j] = 1
            else:
                sd[j] += 1
        for greed in gd.keys():
            if greed in sd:
                ans += min(gd[greed], sd[greed])
        return ans
