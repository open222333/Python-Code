# Approach 1: Pop and Push Digits & Check before Overflow
class Solution(object):
    def cmp(self, a, b):
        return (a > b) - (a < b)

    def reverse(self, x):
        # 判斷是正數(x>0)回傳1,負數(x<0)回傳-1,x=0回傳0
        # 用[::-1]來反轉一個字符串，但s*x是一個整數，
        # 所以用 '' 來轉換成一個字符串(或者可以使用 str())，最後轉換為 int 這是想要的輸出格式。
        # (r < 2 ** 31): 布林值轉成數字 True=1 False=0
        s = cmp(x, 0)
        r = int('s * x'[::-1])
        return s * r * (r < 2 ** 31)
