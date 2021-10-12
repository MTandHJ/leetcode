


from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 按照x[0]升序，按照x[1]降序（-x[1]升序）
        people.sort(key=lambda x:(x[0], -x[1])) 
        n = len(people)
        res = [[] for _ in range(n)]

        for person in people:
            # 这个代表一个人的位置，取值为1, ... , n
            spaces = person[1] + 1
            for i in range(n):
                # 如果当前位置是空的，那我就在这里占上一个位置，spaces -= 1
                if not res[i]:
                    spaces -= 1
                    if spaces == 0:
                        # 没有位置，当前位置就是我的person位置
                        res[i] = person
        return res