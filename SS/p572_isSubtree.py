
from typing import TextIO


class TreeNode:
    def __init__(self, left=None, right=None, val=0) -> None:
        self.left = left
        self.right = right
        self.val = val
    

class Solution:
    def isSubtree(self, root:TreeNode, subroot: TreeNode) -> bool:
        if not root:
            return False
        return self.isSubtreeWithRoot(root, subroot) \
            or self.isSubtreeWithRoot(root.left, subroot) \
                or self.isSubtreeWithRoot(root.right, subroot)
        
    # 判断这两棵树想不想等
    def isSubtreeWithRoot(self, root, subroot):
        if not root and not subroot:
            return True
        
        if not root or not subroot:
            return False
        if root.val != subroot.val:
            return False
        
        return self.isSubtreeWithRoot(root.left, subroot.left) \
            and self.isSubtreeWithRoot(root.right, subroot.right)


class Solution:
    def isSubtree(self, root: TreeNode, subTree: TreeNode):
        if not root:
            return False
        return self.isSubtreeWithRoot(root, subTree) \
            or self.isSubtree(root.left, subTree) \
                or self.isSubtree(root.right, subTree)
        
    
    def isSubtreeWithRoot(self, root: TreeNode, subTree: TreeNode):
        # res = 0
        if not root and not subTree:
            return True
        if not root or not subTree:
            return False
        if root.val != subTree.val:
            return False
        return self.isSubtreeWithRoot(root.left, subTree.left) \
            and self.isSubtreeWithRoot(root.right, subTree.right)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not root:
            return False
        # check
        # 这棵树，和另外一颗是否相等
        # NOTE: 下面的两个条件,是用当前的isSubTree来判断
        # 这棵树的左树和右边的是否相等
        # 这棵树的右树,和subTree是否相等
        return self.isSubtreeWithRoot(root, subRoot) \
        or self.isSubtree(root.left, subRoot) \
        or self.isSubtree(root.right, subRoot)
    
    # 从每个元素出发, 判断两棵树是否相等
    def isSubtreeWithRoot(self, root, subRoot):
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if root.val != subRoot.val:
            return False
        # 递归向下判断
        return self.isSubtreeWithRoot(root.left, subRoot.left) \
        and self.isSubtreeWithRoot(root.right, subRoot.right)
        