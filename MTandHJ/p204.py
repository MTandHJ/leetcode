

from typing import List

from base import version


class Solution:

    @version("3956ms, 69.4mb")
    def countPrimes(self, n: int) -> int:
        primes = [1 for i in range(n)]
        ans = 0
        for i in range(2, n):
            if primes[i]:
                ans += 1
                for j in range(i * i, n, i):
                    primes[j] = 0
        return ans

