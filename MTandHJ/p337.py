

from typing import Optional

from base import version


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    @version("56ms, 17.7mb")
    def rob(self, root: TreeNode) -> int:
        memory = {None: 0}
        def dfs(root):
            if root in memory: return memory[root]
            if root is None: return 0
            if not (root.left or root.right):
                nxt = root.val
            else:
                left1 = left2 = right1 = right2 = 0
                if root.left:
                    left1 = dfs(root.left)
                    left2 = dfs(root.left.left) + dfs(root.left.right)
                if root.right:
                    right1 = dfs(root.right)
                    right2 = dfs(root.right.left) + dfs(root.right.right)
                nxt = max(left1 + right1, left2 + right2 + root.val)
            memory[root] = nxt
            return memory[root]
        return dfs(root)

