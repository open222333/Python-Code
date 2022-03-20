import re

# 函數	說明
# compile(pattern)	以配對形式字串 pattern 當參數，回傳 re.compile() 物件。
# search(pattern, string, flags=0)	從 string 中找尋第一個配對形式字串 pattern ，找到回傳配對物件，沒有找到回傳 None 。
# match(pattern, string, flags=0)	判斷配對形式字串 pattern 是否與 string 的開頭相符，如果相符就回傳配對物件，不相符就回傳 None 。
# fullmatch(pattern, string, flags=0)	判斷 string 是否與配對形式字串 pattern 完全相符，如果完全相符就回傳配對物件，不完全相符就回傳 None 。
# split(pattern, string, maxsplit=0, flags=0)	將 string 以配對形式字串 pattern 拆解，結果回傳拆解後的串列。
# findall(pattern, string, flags=0)	從 string 中找到所有的 pattern ，結果回傳所有 pattern 的串列。
# finditer(pattern, string, flags=0)	從 string 中找到所有的 pattern ，結果回傳所有 pattern 的迭代器。
# sub(pattern, repl, string, count=0, flags=0)	依據 pattern 及 repl 對 string 進行處理，結果回傳處理過的新字串。
# subn(pattern, repl, string, count=0, flags=0)	依據 pattern 及 repl 對 string 進行處理，結果回傳處理過的序對。
# escape(pattern)	將 pattern 中的特殊字元加入反斜線，結果回傳新字串。
# purge()	清除正規運算式的內部緩存。

# testdata = ['https://www.example.com/25213/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b9%82%e0%b8%9b%e0%b9%8a%e0%b9%84%e0%b8%97%e0%b8%a2%e0%b8%a5%e0%b9%88%e0%b8%ad%e0%b8%ab%e0%b8%b5%e0%b8%82%e0%b8%ad%e0%b8%87%e0%b8%aa%e0%b8%b2%e0%b8%a7%e0%b8%99/', 'https://www.example.com/25152/%e0%b8%ab%e0%b8%99%e0%b8%b1%e0%b8%87%e0%b9%82%e0%b8%9b%e0%b9%8a%e0%b9%84%e0%b8%97%e0%b8%a2%e0%b8%84%e0%b8%99%e0%b8%ab%e0%b8%99%e0%b8%b8%e0%b9%88%e0%b8%a1%e0%b8%aa%e0%b8%b2%e0%b8%a7%e0%b9%84%e0%b8%9b/']
# rule = r"[a-zA-Z]+://[^\s]*[$;]"
# for i in testdata:
#     m = re.search(rule ,i)
#     print(m.group().replace("');", ""))

# for data in testdata:
#     da = re.search(r"[a-zA-Z]+://[^\s']*", data)
#     print(da.group(), type(da))


# for data in testdata:
#     pattern = r"[a-zA-Z]+://+[^\s]+\/[\d]{1,10}\/"
#     # da = re.search(pattern, data)
#     da = re.findall(pattern, data)
#     print(da)

test = 'awdwdawd-00101'
print(int(re.findall(r'\d{5}', test)[0]))
