



from typing import List

from base import version


class Solution:

    @version(">=:36ms, 15.2mb")
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        queue = []
        for item in people:
            queue.insert(item[1], item)
        return queue

    @version(">:")
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], -x[1]))
        queue = []
        for item in people:
            queue.insert(item[1], item)
        return queue

    @version("392ms, 15.1mb")
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (x[0], -x[1]))
        queue = [None for _ in range(len(people))]
        for item in people:
            k = item[1]
            loc = -1
            while k >= 0:
                loc -= 1
                if queue[loc] is None:
                    k -= 1
            queue[loc] = item
        return queue