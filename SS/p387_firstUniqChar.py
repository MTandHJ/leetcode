import collections
class Solution:
    # 缺陷:总是需要遍历所有的链表, 时间复杂度较高
    def firstUniqChar(self, s: str) -> int:
        # 计数
        s_count = collections.Counter(s)

        # 找到计数为1, 且最小的索引
        res = len(s)
        for key in s_count:
            if s_count[key] == 1 and s.index(key) <= res:
                res = s.index(key)
        
        # 如果没有找到 s_count[key] == 1
        # 则是-1
        return -1 if res == len(s) else res
    
    def firstUniqChar(self, s: str) -> int:
        # 使用一个不完全遍历的,一找到就退出
        s_count = collections.Counter(s)
        for i, v in enumerate(s):
            if s_count[v] == 1:
                return i
        return -1