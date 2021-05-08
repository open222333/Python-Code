class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left_node = 0
        output = 0
        for right_node in range(len(s)):
            if s[right_node] not in seen:
                output = max(output, right_node-left_node+1)
            else:
                if seen[s[right_node]] < left_node:
                    output = max(output, right_node-left_node+1)
                else:
                    left_node = seen[s[right_node]] + 1
            seen[s[right_node]] = right_node
        return output
