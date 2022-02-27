

from typing import Optional

from base import version


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    @version("dfs: 36ms, 14.8")
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        def dfs(root, val):
            if root is None: return float('inf')
            if root.val != val:
                return root.val
            return min(dfs(root.left, val), dfs(root.right, val))
        smallest = dfs(root, root.val)
        if smallest != float('inf'):
            return smallest
        else:
            return -1
