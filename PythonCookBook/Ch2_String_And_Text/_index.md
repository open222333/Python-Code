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