

from typing import Optional

from base import version


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    @version("48ms, 17.2mb")
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def search(root):
            if root is None: return 0, 0
            depth_left, path_left = search(root.left)
            depth_right, path_right = search(root.right)
            depth = max(depth_left, depth_right) + 1
            path = max(depth_left + depth_right + 1, path_left, path_right)
            return depth, path
        return search(root)[1] - 1
