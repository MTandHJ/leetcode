

from typing import Optional, List

from base import version

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def dfs(root):
            if root is None: return []
            return dfs(root.left) + [root.val] + dfs(root.right)
        nums = dfs(root)
        for i, num in enumerate(nums):
            if (k - num) in nums[i + 1:]:
                return True
        return False
       
