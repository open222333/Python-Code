from banks1 import Banks  # 導入banks模組的Banks類別
from shilin_banks import Shilin_Banks  # 導入shilin_banks模組的Shilin_Banks類別

jamesbank = banks.Banks('James')  # 定義Banks類別物件
print("James's banks = ", jamesbank.bank_title())  # 列印銀行名稱
jamesbank.save_money(500)  # 存錢
jamesbank.get_balance()  # 列出存款金額
hungbank = banks.Shilin_Banks('Hung')  # 定義Shilin_Banks物件
print("Hung's banks = ", hungbank.bank_title())  # 列銀銀行名稱
