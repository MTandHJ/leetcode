

from typing import Optional

from base import version


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    @version("444ms, 16.3mb")
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        count = [0]
        pathSums = []
        def dfs(root):
            if root is None: return 
            pathSums.append(0)
            for i in range(len(pathSums)):
                pathSums[i] += root.val
                if pathSums[i] == targetSum:
                    count[0] += 1
            dfs(root.left)
            dfs(root.right)
            pathSums.pop()
            for i in range(len(pathSums)):
                pathSums[i] -= root.val
            return
        dfs(root)
        return count[0]