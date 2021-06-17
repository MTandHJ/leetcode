class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # hash表方法
        hashmap1 = {}
        hashmap2 = {}
        for s1, t1 in zip(s, t):
            # 建立一次对应关系之后，发现于原来的不一致
            # （原来存在过，但是这个是新的）
            if hashmap1.get(s1, t1) != t1 or hashmap2.get(t1, s1) != s1:
                return False
            #  建立对应关系
            hashmap1[s1] = t1
            hashmap2[t1] = s1
        return True

    def isIsomorphic(self, s: str, t: str) -> bool:
        # index方法
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                # 比如'egg' 'bag'
                if s.index(s[i]) != t.index(t[i]):
                    return False
            return True