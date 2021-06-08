# 數字轉換成羅馬數字
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
class Solution():
    def intToRoman(self, num: int) -> str:
        roman = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
                 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        romanized = ''
        for base, symb in roman.items():
            romanized += symb * (num // base) # 將符號記錄進 romanized
            num %= base  # 取餘數 繼續迴圈 直到數字等於0
        else:
            return romanized
