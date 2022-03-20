class SettlementScheme():
    '''順序賠付'''

    def __init__(self, money: list, bet: list) -> None:
        self.betMakerMoneyList = money
        self.betAmountList = bet

    def SequentialSettlement(self):
        for betAmount in self.betAmountList:
            a = 0
            totalMoney = 0
            while True:
                totalMoney += self.betMakerMoneyList[a]
                if totalMoney < betAmount:
                    self.betMakerMoneyList[a] -= self.betMakerMoneyList[a]
                else:
                    amount = totalMoney - betAmount
                    settleAmount = self.betMakerMoneyList[a] - amount
                    self.betMakerMoneyList[a] = amount
                    break
                a += 1
        return


betMaker = [10000, 5000, 1000000000]
betmoneylist = [[6000, 6000, 1000, 1500, 10000, 10000], [
    6000, 6000, 1000, 1500, 10000, 10000], [6000, 6000, 1000, 1500, 10000, 10000]]

print(betMaker)
for betmoney in betmoneylist:
    a = 0
    totalMoney = 0
    settleCount = []
    while True:
        totalMoney += betMaker[a]
        if totalMoney < betmoney:
            settleCount.append(betMaker[a])
            betMaker[a] -= betMaker[a]
        else:
            BMamount = totalMoney - betmoney
            settleAmount = betMaker[a] - BMamount
            betMaker[a] = BMamount
            settleCount.append(settleAmount)
            bm = 1
            for s in settleCount:
                if s is not 0:
                    print(f"第{bm}位，賠{s}")
                bm += 1
            break
        a += 1
