'''
2.10 在正規表達式中處理Unicode字元
* 問題：使用正規表達式處理文字，但對Unicode有疑慮。
* 解法：re模組，已納入某些Unicode字元類別的基礎知識。執行比對與搜尋動作時，先把所有的文字正規化或淨化(sanitize)為一種標準行事。(參閱訣竅2.9)
* 討論：若將Unicode與正規表達式混合一起使用，可使用第三方regex程式庫(http://pypi.python.org/pypi/regex)。
'''
import re

num = re.compile('\d+')
# ASCII數字
print(num.match('123'))
# 阿拉伯數字
print(num.match('\u0661\u0662\u0663'))

# 以下regex能匹配幾個不同的阿拉伯code pages(代碼頁)中的所有字元
arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')
pat = re.compile('stra\u00dfe', re.IGNORECASE)
s = 'straβe'
print(pat.match(s))
pat.match(s.upper())  # 不匹配
print(s.upper())
