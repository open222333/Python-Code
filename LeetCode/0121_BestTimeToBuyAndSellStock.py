# Approach 1: Brute Force
# Approach 2: One Pass

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        '''Approach 2: One Pass'''
        minprice = max(prices)
        maxprofit = 0  # 最大利潤
        for i in range(len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            # maxprofit = max(maxprofit, prices[i] - minprice)
            elif prices[i] - minprice > maxprofit:
                maxprofit = prices[i] - minprice
        return maxprofit


# prices = [7, 1, 5, 3, 6, 4]
prices = [2, 4, 1]
print(Solution().maxProfit(prices))
