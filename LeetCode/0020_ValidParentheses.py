# {} [] () 要有完整的括號配對
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        leftSide = ["{", "[", "("]
        rightSide = ["}", "]", ")"]
        for c in s:
            if c in leftSide:
                stack.append(c)
            elif c in rightSide:
                if len(stack) == 0:
                    return False
                else:
                    if stack.pop() is leftSide[rightSide.index(c)]:
                        pass
                    else:
                        return False
        return len(stack) == 0


print(Solution().isValid("("))
