class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        # Time Limit Exceeded
        ans = []
        for i in timeSeries:
            temp = []
            for j in range(duration):
                temp.append(i + j)
            for k in temp:
                ans.append(k)
        return len(set(ans))

    def findPoisonedDuration2(self, timeSeries: list[int], duration: int) -> int:
        # Approach 1: One pass
        if len(timeSeries) == 0:
            return 0
        ans = 0  # 總計中毒時間
        for i in range(len(timeSeries) - 1):
            # 取 間隔長度和中毒區間之中的最小值
            ans += min(timeSeries[i + 1] - timeSeries[i], duration)
        # 加入最後一個攻擊的秒數
        return ans + duration


timeSeries = [1, 4]
duration = 2
print(Solution().findPoisonedDuration2(timeSeries, duration))
