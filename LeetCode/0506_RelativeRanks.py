class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        # 自己的解法
        rank = sorted(score, reverse=True)
        ans = []
        for i in range(len(score)):
            ranknum = rank.index(score[i]) + 1
            if ranknum == 1:
                ans.append("Gold Medal")
            elif ranknum == 2:
                ans.append("Silver Medal")
            elif ranknum == 3:
                ans.append("Bronze Medal")
            else:
                ans.append(str(ranknum))
        return ans

    def findRelativeRanks2(self, score: list[int]) -> list[str]:
        # 更快
        rank = sorted(score, reverse=True)
        ans = {}
        for ranknum, num in enumerate(rank):
            if ranknum == 0:
                ans[num] = "Gold Medal"
            elif ranknum == 1:
                ans[num] = "Silver Medal"
            elif ranknum == 2:
                ans[num] = "Bronze Medal"
            else:
                ans[num] = str(ranknum + 1)
        return [ans[i] for i in score]


score = [10, 3, 8, 9, 4]
print(Solution().findRelativeRanks2(score))
