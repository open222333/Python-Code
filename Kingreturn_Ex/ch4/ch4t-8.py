# 重新設計 ch2_5.py
# 銀行存款複利的計算 假設目前銀行年利率是1.5% 複利公式：本金和＝本金＊（１＋年例率）＾Ｎ ＃Ｎ是年
# 一筆５萬元 計算５年後本金和
years = int(input("請輸入年數："))
yearrate = float(input("請輸入年利率："))
money = 50000 * (1 + (yearrate / 100)) ** years
print('本金和是：%6.0f' % money)
