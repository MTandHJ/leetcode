

from typing import List
from collections import defaultdict

from base import version

class Solution:

    @version("792ms, 15.8mb")
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        def gen():
            while True:
                yield hand[0]
        gener = gen()
        while True:
            try:
                seed = next(gener)
                for integer in range(seed, seed + groupSize):
                    hand.remove(integer)
            except ValueError:
                return False
            except IndexError:
                return True

    @version("80ms, 16.4mb")
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        pool = defaultdict(int)
        for card in hand:
            pool[card] += 1
        for card in pool.keys():
            nums = pool[card]
            if nums == 0:
                continue
            for x in range(card, card + groupSize):
                if pool[x] == 0:
                    return False
                pool[x] -= nums
        return True


test = Solution()
print(test.isNStraightHand(
    [1,2,3,6,2,3,4,7,8],
    3
))
