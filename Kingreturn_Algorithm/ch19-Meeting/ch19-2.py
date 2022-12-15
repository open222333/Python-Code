# 回文演算法(palindrome)
from collections import deque


def palindrome(word):
    '''測試是否回文'''
    wd = deque(word)
    while len(wd) > 1:
        if wd.pop() != wd.popleft():
            return False
    return True
