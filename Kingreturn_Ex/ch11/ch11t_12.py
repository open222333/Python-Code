def isPalindrome(s):
    a = ''.join(i for i in str(s)[::-1])
    if a == str(s):
        return True
    else:
        return False


string = input("請輸入內容(判斷是否回文字串)：")
print('%s 是否為回文字串：' % string, isPalindrome(string))
