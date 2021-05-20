# Given a string s, return the longest palindromic substring in s
# Approach 1: Longest Common Substring
# Approach 2: Brute Force
# Approach 3: Dynamic Programming
# Approach 4: Expand Around Center
# Approach 5: Manacher's Algorithm


class Solution_OldCodingFarmer():
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            res = max(self.helper(s, i, i), self.helper(
                s, i, i + 1), res, key=len)

        return res

    # get the longest palindrome, l, r are the middle indexes
    # from inner to outer

    def helper(self, s, l_index, r):
        while 0 <= l_index and r < len(s) and s[l_index] == s[r]:
            l_index -= 1
            r += 1
        return s[l_index + 1: r]
