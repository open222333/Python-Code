# Given a string s, return the longest palindromic substring in s
# Approach 1: Longest Common Substring
# Approach 2: Brute Force
# Approach 3: Dynamic Programming
# Approach 4: Expand Around Center
# Approach 5: Manacher's Algorithm

class Solution5():
    # Manacher algorithm
    # http://en.wikipedia.org/wiki/Longest_palindromic_substring

    def longestPalindrome(self, s):
        transString = '#'.join('^{}$'.format(s))  # 在字串的字元間加上# ^$是邊界
        # S = "abba", T = "^#a#b#b#a#$"
        n = len(transString)
        palindromeL = [0] * n
        centerP = rightP = 0
        for i in range(1, n - 1):
            palindromeL[i] = (rightP > i) and min(
                rightP - i, palindromeL[2 * centerP - i])
            # 以i為中心向外展開
            while transString[i + 1 + palindromeL[i]] == \
                    transString[i - 1 - palindromeL[i]]:
                palindromeL[i] += 1
            if i + palindromeL[i] > rightP:
                centerP, rightP = i, i + palindromeL[i]

        maxLen, centerIndex = max((n, i) for i, n in enumerate(palindromeL))
        return s[(centerIndex - maxLen) // 2: (centerIndex + maxLen) // 2]


class Solution_OldCodingFarmer():
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            res = max(self.helper(s, i, i), self.helper(
                s, i, i + 1), res, key=len)

        return res

    # get the longest palindrome, l, r are the middle indexes
    # from inner to outer

    def helper(self, s, left, right):
        # right left 由內到外 比對是否為相同字元
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]
