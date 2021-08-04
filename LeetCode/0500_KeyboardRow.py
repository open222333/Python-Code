class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        keyboardRow = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        ans = []
        for word in words:
            for row in keyboardRow:
                if word[0].lower() in row:
                    for i in range(1, len(word)):
                        if word[i].lower() not in row:
                            break
                    else:
                        ans.append(word)
        return ans


# words = ["Hello", "Alaska", "Dad", "Peace"]
words = ["Aasdfghjkl", "Qwertyuiop", "zZxcvbnm"]
print(Solution().findWords(words))
