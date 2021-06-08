# 羅馬數字轉換成數字
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
class Solution():
    def romanToInt(self, s: str) -> int:
        res, prev = 0, 0
        romanDict = {'I': 1, 'V': 5, 'X': 10,
                     'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in s[::-1]:
            if romanDict[i] >= prev:
                res += romanDict[i]
            else:
                res -= romanDict[i]  # "IV" --> 5-1, "IX" --> 10 -1
            prev = romanDict[i]
        return res


roman = Solution()
strR = input("Input:")
print(roman.romanToInt(strR))
