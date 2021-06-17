from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hashmap1 = dict((v, i) for i, v in enumerate(list1))
        hashmap2 = dict((v, i) for i, v in enumerate(list2))

        # 所有可能的相交元素
        union_set = {}
        for key in hashmap1:
            if key in hashmap2:
                union_set[key] = hashmap1[key] + hashmap2[key]
        
        # 找到最小的索引值
        min_idx = len(list1) + len(list2)
        for key, val in union_set.items():
            if val < min_idx:
                min_idx = val
        
        # 找到最小索引和对应的key
        res = []
        for key, val in union_set.items():
            if val == min_idx:
                res.append(key)
        return res

        # 不懂为什么后面的为什么不对
        # 初看好像官方题解有一个类似的
        # TODO: 把这个搞好
        # res = []
        # min_idx = max(len(list1), len(list2))
        # for key in hashmap1:
        #     if key in hashmap2:
        #         tmp_sum = hashmap1[key] + hashmap2[key]
        #         if tmp_sum < min_idx:
        #             res = [key]
        #             min_idx = tmp_sum
        #         elif tmp_sum == min_idx:
        #             res.append(key)
        # return res
    
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # 从评论区学习一个
        # defaultdict(list), min(hashmap.keys()), a.index(a[i])
        pass


import collections
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # 为列表2创建一个列表
        set2 = set(list2)
        hashset = collections.defaultdict(list)
        # (索引和: key) 对
        for i, s1 in enumerate(list1):
            if s1 in set2:
                hashset[i + list2.index(s1)].append(s1)
        minkey = min(hashset.keys())
        return hashset[minkey]

