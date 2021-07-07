# Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        for i in arr:
            if i == 0:
                arr.remove(i)
                if 0 in arr:
                    return True
                else:
                    pass
            elif (i * 2) in arr:
                print(i)
                return True
        return False

    def checkIfExist2(self, arr: list[int]) -> bool:
        for i in range(len(arr)):
            if arr[i] * 2 in arr and arr.index(arr[i] * 2) != i:
                return True
        return False
        
arr = [-2,0,10,-19,4,6,-8]
print(Solution().checkIfExist2(arr))