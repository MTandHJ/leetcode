

from typing import Optional

from base import version


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    @version("40ms, 17.2mb")
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    @version("40ms, 16.2mb")
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        depth = 0
        cur = [root]
        while cur:
            depth += 1
            nxt = []
            for node in cur:
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            cur= nxt
        return depth