class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        charmap = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        ans = []
        digitsList = []
        for i in list(digits):
            digitsList.append(list(charmap[i]))
        if len(digitsList) == 0:
            pass
        elif len(digitsList) > 4:
            pass
        elif "0" in list(digits) or "1" in list(digits):
            pass
        else:
            ans = digitsList[0]
            for i in range(1, len(digitsList)):
                ans = self.combinationList(ans, digitsList[i])
        return ans

    def combinationList(self, listA: list, listB: list):
        result = []
        for i in listA:
            for j in listB:
                result.append(i + j)
        return result
