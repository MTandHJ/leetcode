

from typing import List

from base import version

class Solution:

    @version("over")
    def checkPerfectNumber(self, num: int) -> bool:
        the_sum = 0
        for i in range(num):
            if num % i == 0:
                the_sum += i
        if the_sum == num:
            return True
        else:
            return False

    @version("40ms, 15.1mb")
    def checkPerfectNumber(self, num: int) -> bool:
        left, right = 1, int(num ** 0.5)
        the_sum = 1
        while left < right:
            left += 1
            if num % left == 0:
                the_sum += left + num / left
                right = min(num / left - 1, right)
        return the_sum == num

    @version("36ms, 15.1mb")
    def checkPerfectNumber(self, num: int) -> bool:
        pool = {1}
        def search(num):
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    for item in set(pool):
                        pool.add(item * i)
                    return search(num // i)
            for item in set(pool):
                pool.add(item * num)
        search(num)
        pool.remove(num)
        return sum(pool) == num

