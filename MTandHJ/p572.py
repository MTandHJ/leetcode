

from typing import Optional

from base import version


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    @version("124ms, 16.3mb")
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def check(root, subRoot):
            if root is None and subRoot is None: return True
            if root is None or subRoot is None: return False
            if root.val != subRoot.val: return False
            return (check(root.left, subRoot.left) and check(root.right, subRoot.right))
        if root is None: return False
        if root.val == subRoot.val and check(root, subRoot): return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

