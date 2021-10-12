


from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int):
        def dfs(candidates: List[int], target: int, ans: List[List[int]], combine: List[int], idx: int):
            if idx == len(candidates):
                return
            # 满足条件，添加进去 
            if target == 0:
                ans.append(combine)
                return 
            # 不选择当前数
            dfs(candidates, target, ans, combine, idx + 1)
            # 选择当前数， 并且在当前节点下进行回溯：选择、不选择
            if target - candidates[idx] >= 0:
                combine.append(candidates[idx])
                dfs(candidates, target - candidates[idx], ans, combine, idx)
                combine.pop()
        
        ans = []
        combine = []
        dfs(candidates, target, ans, combine, 0)
        return ans