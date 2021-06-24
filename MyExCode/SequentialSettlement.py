class SequentialSettlement():
    def __init__(self, *money, **bet) -> None:
        self.betmakerMoneyList = []
        self.betList = []
        for i in money:
            self.betmakerMoneyList.append(i)
        for j in bet:
            self.betList.append(j)

    def getBetMakerMoney(self):
        return self.betmakerMoneyList

    def getBetList(self):
        return self.betList


betMaker = SequentialSettlement(10000, 10000, 1000000).getBetMakerMoney()
betList = SequentialSettlement(10000, 10000, 1000000,[12000, 1700, 1000, 1500]).getBetList()
print(betMaker)
print(betList)
betmoneylist = [12000, 1700, 1000, 1500]

for betmoney in betmoneylist:
    a = 0
    totalMoney = 0
    while True:
        totalMoney += betMaker[a]
        if totalMoney < betmoney:
            betMaker[a] -= betMaker[a]
        else:
            amount = totalMoney - betmoney
            settleAmount = betMaker[a] - amount
            betMaker[a] = amount
            break
        a += 1
