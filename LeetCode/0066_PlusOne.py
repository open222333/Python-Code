class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        num = 0
        digit = len(digits) - 1
        for i in range(len(digits)):
            num += (digits[i] * (10 ** digit))
            digit -= 1

        # num += 1
        # ans = []
        # for j in str(num):
        #     ans.append(j)
        return [ans for ans in str(num + 1)]

    def plusOne_Fast(self, digits: list[int]) -> list[int]:
        num = ''.join(str(digits).lstrip('[').rstrip(']').split(', '))  # [1,2,3] -> '123'
        return [i for i in str(int(num) + 1)]


# digits = [4, 3, 2, 1]
digits = [1, 2, 3]
text = Solution().plusOne(digits)
# text = Solution().plusOne_Fast(digits)
print(text)
