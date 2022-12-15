def isPalindrome(s):
    """判斷輸入數值受否為回文(Palindrome)數字"""
    s = str(s)
    a = ''.join(i for i in s[::-1])
    print(a)
    if s == a:
        return True
    else:
        return False


x = eval(input("請輸入數字，判斷是否為回文數字："))
print(isPalindrome(x))
