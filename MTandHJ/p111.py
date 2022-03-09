

from typing import Optional

from base import version


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    @version("bfs: 424ms, 51.5mb")
    def minDepth(self, root: TreeNode) -> int:
        if root is None: return 0
        cur = {root}
        depth = 0
        while cur:
            depth += 1
            nxt = set()
            for node in cur:
                if node.left:
                    nxt.add(node.left)
                if node.right:
                    nxt.add(node.right)
                if not (node.left or node.right):
                    return depth
            cur = nxt
        return depth

    @version("dfs: 664ms, 56.3mb")
    def minDepth(self, root: TreeNode) -> int:
        def dfs(root, depth):
            if not (root.left or root.right): return depth
            left = right = float('inf')
            if root.left:
                left = dfs(root.left, depth + 1)
            if root.right:
                right = dfs(root.right, depth + 1)
            return min(left, right)
        if root is None: return 0
        return dfs(root, 1)
