

from typing import Optional

from base import version


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:



    @version("44ms, 14.9mb")
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(root1, root2):
            if root1 == root2: return True
            if root1.val != root2.val: return False
            assert check(root1.left, root2.right)
            assert check(root1.right, root2.left)
            return True
        try:
            return check(root.left, root.right)
        except AssertionError:
            return False
        except AttributeError:
            return False

