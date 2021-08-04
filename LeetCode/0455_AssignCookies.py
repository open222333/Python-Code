class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        # Two Points
        g.sort()
        s.sort()
        i = j = 0
        out = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
                out += 1
            j += 1
        return out
