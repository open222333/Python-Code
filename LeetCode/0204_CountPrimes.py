class Solution:
    def countPrimes(self, n: int) -> int:
        primes = []
        if n > 2:
            primes.append(2)
        for i in range(3, n):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                primes.append(i)
        return len(primes)

    # https://leetcode.com/problems/count-primes/discuss/1353496/Count-Primes-for-Kids!-_(-)_

    def countPrimes2(self, n: int) -> int:
        primes = [True] * n
        primes[0] = primes[1] = False
        if n < 2:
            return 0
        for num in range(2, n):
            if primes[num]:
                for multiple in range(2 * num, n, num):
                    primes[multiple] = False
        return sum(primes)


print(Solution().countPrimes2(10000))
