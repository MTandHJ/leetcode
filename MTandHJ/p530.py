

from typing import Optional, List

from base import version

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def getMinimumDifference(self, root: TreeNode) -> int:
        def dfs(root):
            if root is None: return []
            return dfs(root.left) + [root.val] + dfs(root.right)
        nums = dfs(root)
        theMin = float('inf')
        for i in range(len(nums) - 1):
            theMin = min(theMin, nums[i + 1] - nums[i])
        return theMin

