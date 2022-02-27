

from typing import Optional

from base import version


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    @version("44ms, 19.8mb")
    def isBalanced(self, root: TreeNode) -> bool:
        def maxDepth(root):
            if root is None: return 0
            left = maxDepth(root.left)
            right = maxDepth(root.right)
            if abs(left - right) > 1:
                raise ValueError
            else:
                return max(left, right) + 1
        try:
            maxDepth(root)
            return True
        except ValueError:
            return False
