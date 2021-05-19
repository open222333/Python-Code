"""
Given a string s, find the length of the longest substring without repeating
 characters.
"""


# Approach 1: Brute Force 暴力解法
class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def check(start, end):
            chars = [0] * 128
            for i in range(start, end + 1):
                c = s[i]
                chars[ord(c)] += 1
                if chars[ord(c)] > 1:
                    return False
            return True

        n = len(s)

        res = 0
        for i in range(n):
            for j in range(i, n):
                if check(i, j):
                    res = max(res, j - i + 1)
        return res


# Approach 2: Sliding Window
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [0] * 128
        left = right = 0
        res = 0
        while right < len(s):
            r = s[right]
            chars[ord(r)] += 1

            while chars[ord(r)] > 1:
                r = s[left]
                chars[ord(1)] -= 1
                left += 1
            res = max(res, right - left + 1)

            right += 1
        return res


# Approach 3: Sliding Window Optimized
class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        mp = {}  # mp stores the current index of a character
        i = 0
        for j in range(n):  # try to extend the range [i, j]
            if s[j] in mp:
                i = max(mp[s[j]], i)

            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1

        return ans


# https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/347818/Python3%3A-sliding-window-O(N)-with-explanation
class Solution_zhanweiting:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}  # 儲存{字母：索引值} seen[charactor] = index
        left_pointer = 0  # 左邊指針從0開始
        output = 0  # 窗口大小
        for right_pointer in range(len(s)):
            # 如果右指針的字元不在字典內
            if s[right_pointer] not in seen:
                # 取output跟目前窗口大小(r-l+1)的最大值
                output = max(output, right_pointer - left_pointer + 1)
            # 如果右指針的字元在字典內
            else:
                if seen[s[right_pointer]] < left_pointer:
                    # 取output跟目前窗口大小(r-l+1)的最大值
                    output = max(output, right_pointer - left_pointer + 1)
                # 若有相同字元且右指針字元的索引值大於左指針
                else:
                    # 則左指針移動到目前右指針的右邊一位
                    left_pointer = seen[s[right_pointer]] + 1
            # 儲存{字母：索引值} seen[charactor] = index ,字元加入字典
            seen[s[right_pointer]] = right_pointer
        return output


class Solution_:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        usedChar = {}  # 儲存{字母：索引值} seen[charactor] = index
        for i in range(len(s)):
            # 字元已在字典內 且 字元的索引值大於等於start
            if s[i] in usedChar and start <= usedChar[s[i]]:
                # 移動start指針
                start = usedChar[s[i]] + 1
            else:
                # 窗口大小
                maxLength = max(maxLength, i - start + 1)
            # 字元加入字典
            usedChar[s[i]] = i
        return maxLength
