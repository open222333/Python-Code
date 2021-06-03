# 判斷是否回文
# Approach 1: Revert half of the number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        y = "".join(reversed(x))
        if x == y:
            return True
        else:
            return False
