from typing import List
import collections

class Solution:
    # 排序
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)

        for st in strs:
            cur = ''.join(sorted(st))
            mp[cur].append(st)
        
        return list(mp.values())

    # 计数
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)

        for st in strs:
            counts = [0] * 26
            for ch in st:
                counts[ord(ch) - ord('a')] += 1
            mp[tuple(counts)].append(st)
        return list(mp.values())
    
    # 数字相乘
    def groupAnagrams3(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        ans = collections.defaultdict(list)
        prime = [
            2, 3, 5, 7, 
            11, 13, 17, 19, 
            23, 29, 31, 41, 43, 47,
            53, 59, 61, 67,
            71, 73, 79, 83, 89,
            91, 97, 101, 103]
        mod = 1e9 + 7
        for i in range(n):
            hash = 1
            for j in range(len(strs[i])):
                num = ord(strs[i][j]) - 97
                hash = ((hash % mod) * (prime[num] % mod)) % mod
                hash = int(hash)
            
            if not ans[hash]:
                ans[hash] = []
            ans[hash].append(strs[i])
        return list(ans.values())

ins = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(ins.groupAnagrams3(strs))