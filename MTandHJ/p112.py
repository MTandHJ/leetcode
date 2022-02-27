

from typing import Optional

from base import version


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    @version("dfs: 52ms, 16.2mb")
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, pathsum):
            if root is None: return False
            pathsum += root.val
            if pathsum == targetSum and not (root.left or root.right):
                raise ValueError
            dfs(root.left, pathsum)
            dfs(root.right, pathsum)
            return False
        try:
            return dfs(root, 0)
        except ValueError:
            return True

    @version("36ms, 16.1mb")
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None: return False
        cur = [(root, root.val)]
        while cur:
            nxt = []
            for node, nodeSum in cur:
                if node.left:
                    nxt.append((node.left, nodeSum + node.left.val))
                if node.right:
                    nxt.append((node.right, nodeSum + node.right.val))
                if not (node.left or node.right) and nodeSum == targetSum:
                    return True
            cur = nxt
        return False

