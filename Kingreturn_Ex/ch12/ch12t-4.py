class Banks():
    '''定義銀行類別'''

    def __init__(self, uname) -> None:  # 初始化方法
        self.__name = uname  # 設定存款者名字
        self.__twdbalance = 0  # 設定開戶金額是0
        self.__usdbalance = 0  # 設定開戶金額是0
        self.__bankname = 'Taipei Bank'  # 設定銀行名稱
        self.__rate = 30  # 預設美金與台幣換匯比例
        self.__service_charge = 0.01  # 換匯的服務費

    def save_money(self, twd):  # 設計存款方法
        self.__twdbalance += twd  # 執行存款
        print("存款台幣", twd, "完成")  # 列印存款完成

    def withdraw_money(self, twd):  # 設計提款方法
        self.__twdbalance -= twd  # 執行提款
        print("提款台幣", twd, "完成")  # 列印提款完成

    def get_twdbalance(self):  # 獲得台幣存款餘額
        print(self.__name.title(), '目前台幣存款餘額：', self.__twdbalance)

    def get_usdbalance(self):  # 獲得美金存款餘額
        print(self.__name.title(), '目前美金存款餘額：', self.__usdbalance)

    def usd_to_twd(self, usd):  # 美金兌換台幣的方法
        if usd > self.__usdbalance:
            print("美金額度不足")
        else:
            self.__usdbalance -= usd
            self.__twdbalance += self.__cal_usdtotwd_rate(usd)
            return self.__usdbalance

    def twd_to_usd(self, twd):  # 台幣兌換美金的方法
        if twd > self.__twdbalance:
            print("台幣額度不足")
        else:
            self.__twdbalance -= twd
            self.__usdbalance += self.__cal_twdtousd_rate(twd)
            return self.__twdbalance

    def get_usd(self, usd):
        return self.twd_to_usd(usd * self.__rate / (1 - self.__service_charge))

    def get_twd(self, twd):
        return self.usd_to_twd(twd / self.__rate / (1 - self.__service_charge))

    def __cal_usdtotwd_rate(self, usd):  # 計算換匯 這是私有方法
        return int(usd * self.__rate * (1 - self.__service_charge))

    def __cal_twdtousd_rate(self, twd):  # 計算換匯 這是私有方法
        return int(twd / self.__rate * (1 - self.__service_charge))


tom = Banks('tom')
tom.save_money(5000)
tom.get_twdbalance()
tom.get_usdbalance()
tom.withdraw_money(3000)
tom.get_twdbalance()
tom.get_usdbalance()
tom.save_money(1500)
tom.get_twdbalance()
tom.get_usdbalance()
tom.get_usd(100)
tom.get_twdbalance()
tom.get_usdbalance()
