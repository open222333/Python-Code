class Banks():
    '''定義銀行類別'''

    def __init__(self, uname) -> None:  # 初始化方法
        self.__name = uname  # 設定存款者名字
        self.__balance = 0  # 設定開戶金額是0
        self.__bankname = 'Taipei Bank'  # 設定銀行名稱

    def save_money(self, money):  # 設計存款方法
        self.__balance += money  # 執行存款
        print("存款", money, "完成")  # 列印存款完成

    def withdraw_money(self, money):  # 設計提款方法
        self.__balance -= money  # 執行提款
        print("提款", money, "完成")  # 列印提款完成

    def get_balance(self):  # 獲得存款餘額
        print(self.__name.title(), '目前餘額：', self.__balance)

    def bank_title(self):  # 獲得銀行名稱
        return self.__bankname


class Shilin_Banks(Banks):
    # 定義士林分行
    def __init__(self, uname):
        self.bankname = "Taipei Bank - Shilin Branch"  # 定義分行名稱

    def bank_title(self):  # 獲得銀行名稱
        return self.bankname


class Beitou_Banks(Banks):
    # 定義北投分行
    def __init__(self, uname) -> None:
        self.bankname = "Taipei Bank - Beitou Branch"  # 定義分行名稱

    def bank_title(self):  # 獲得銀行名稱
        return self.bankname


jamesbank = Banks('James')  # 定義Banks類別物件
print("James's banks = ", jamesbank.bank_title())  # 列印銀行名稱
hungbank = Shilin_Banks('Hung')  # 定義Shilin_Banks類別物件
print("Hung's banks = ", hungbank.bank_title())  # 列印銀行名稱
tombank = Beitou_Banks('Tom')
print(tombank.bank_title())
