

from typing import Optional

from base import version


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    @version("dfs: 36ms, 16mb")
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def dfs(root, part):
            if not (root.left or root.right): 
                if part == 'left':
                    return root.val
                else:
                    return 0
            left = dfs(root.left, 'left') if root.left else 0
            right = dfs(root.right, 'right') if root.right else 0
            return left + right
        return dfs(TreeNode(0, right=root), 'right')

    @version("40ms, 15.1mb")
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        cur = [TreeNode(right=root)]
        ans = 0
        while cur:
            nxt = []
            for node in cur:
                if node.left:
                    if not (node.left.left or node.left.right):
                        ans += node.left.val
                    else:
                        nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            cur = nxt
        return ans
