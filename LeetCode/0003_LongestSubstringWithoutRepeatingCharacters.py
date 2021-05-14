# https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/347818/Python3%3A-sliding-window-O(N)-with-explanation

# Given a string s, find the length of the longest substring without repeating
# characters.

class Solution:
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
            # 儲存{字母：索引值} seen[charactor] = index
            seen[s[right_pointer]] = right_pointer
        return output
