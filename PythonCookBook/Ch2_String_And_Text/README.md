# 字串與文字

* 問題：
* 解法：
* 討論：

2.1 依據任意的多個定界符來切分字串
* 問題：需要把一個字串切分(split)成幾個欄位，但字串中界定欄位的定介符(delimiters)以及其周圍的空白數並不一致。
* 解法：字串的split()可解決，若要更多彈性，則可使用re.split()。
* 討論：re.split()，若正則表達式中含有用括號(parentheses)包圍的捕捉組(capture group)，匹配的文字也會出現在結果


2.2 在一個字串的開頭或結尾比對文字
* 問題：需要檢查一個字串的開頭(start)或結尾(end)，以找尋特定的文字模式，例如：副檔名(filename extensions)，URL schemes...
* 解法：
    > 1. 檢查字串開頭或結尾最簡單方式是startswith()、endswith()。多個選項可用元組放入參數。
    > 2. urllib.request urlopen()函式
* 討論：切片與正則表達式都可以解決這問題。

常見的資料縮減(data reductions)作業。
    
    if any(name for name in listdir(os.path.dirname)):
        pass


2.3 使用Shell的通配模式來比對字串
* 問題：使用與Unix shell 底下常使用的通配模式(wildcard patterns，例如:*.py、Dat[0-9]*.csv)來比對文字。
* 解法：
fnmatch模組fnmatch()：與底層的檔案系統(取決於作業系統)相同的大小寫區分規則(case-sensitivity rules)來比對模式。
fnmatch模組fnmatchcase()：區分大小寫。
* 討論：fnmatch的能力介於簡單的字串方法以及強大的正規運算式之間。

2.4 比對與搜尋文字模式
* 問題：在文字中比對(match)或搜尋特定模式(pattern)。
* 解法：
    > 1. 簡單的字面值(literal)：使用字串方法，str.find()、str.endswith()、str.startswith()或類似的方法。
    > 2. 複雜的比對工作：使用正則表達式(regular expressions)。
    >       - match()：匹配接近字串開頭。
    >       - findall()：找出所有符合。
    >       - finditer()：迭代的匹配。
* 討論：正則表達式，使用re.compile()編譯一個模式，再使用match()、findall()、finditer()。

2.5 搜尋並取代文字
* 問題：在一個字串搜尋並取代一個文字模式
* 解法：
    > 1. str.replace()：簡單的可使用此函式。
    > 2. re模組 sub()函式：較為複雜可使用此函式。
    > 3. calendar模組 month_abbr()函式：更複雜可使用此函式。

    > subn():可知道替換了多少地方。
* 討論：

2.6 搜尋並取代不區分大小寫的文字
* 問題：以不區分大小寫(case-insensitive)的方式搜尋並取代文字。
* 解法：re.IGNORECASE(flag)，不區分大小寫的比對。
* 討論：

2.7 為最短匹配指定一個正規表達式
* 問題：使用一個正規表達式(regular expressions)比對一個文字模式(text pattern)，但所識別出來的是符合一個模式的最長匹配，需改成最短匹配。
* 解法：.*加上？ 就會進行最短匹配。
* 討論：

2.8 為多行的模式撰寫一個正規表達式
* 問題：試著使用一個正規表達式(reqular expression)來比對一個區塊(block)，希望比對動作能夠跨越數行。
* 解法：正規表達式的. 不匹配換行字元(newline)。(?:.|\n)指定一個非捕捉組。
* 討論：re.compile() 接受一個旗標 re.DOTALL，用處：匹配所有字元，包含(newline)

2.9 以一種標準表示法正規化Unicode文字
* 問題：正在處理Unicode字串，得確定所有的字串都使用相同的底層表示法。
* 解法：使用unicodedata模組normalize()函式 將文字正規化。NFC代表字元應該是組成完整的。NFD代表字元應該是透過結合字元的使用而完全分解開來。也支援NFKC NFKD形式的正規化。
* 討論：combining()函式測試一個字元是否為一個結合字元。