# Approach 1: Brute Force
# Approach 2: Peak Valley Approach 峰谷方法
# Approach 3: Simple One Pass

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Approach 3: Simple One Pass
        maxprofit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                maxprofit += prices[i] - prices[i - 1]
        return maxprofit

    def maxProfit2(self, prices: list[int]) -> int:
        # Approach 2: Peak Valley Approach 峰谷方法
        i = 0
        peak = prices[0]  # 峰
        vally = prices[0]  # 谷
        maxprofit = 0  # 最大利潤
        while i < len(prices) - 1:
            # 谷
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1
            vally = prices[i]
            # 峰
            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                i += 1
            peak = prices[i]
            maxprofit += peak - vally
        return maxprofit


prices = [7, 1, 5, 3, 6, 4]
print(Solution().maxProfit2(prices))
