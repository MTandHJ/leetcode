
import math

class TreeNode:
    def __init__(self, left=None, right=None, val=0):
        self.left = left
        self.right = right
        self.val = val
    
class Solution:
    def isBalanced(self, root: TreeNode):
        return self.height(root) >= 0
    
    def height(self, root: TreeNode) -> int:
        if not root:
            return 0
        l = self.height(root.left)
        r = self.height(root.right)
        # 底层只要有一个是这样的，就返回-1
        if l == -1 or r == -1 and abs(l - r) > 1:
            return -1
        
        return max(l, r) + 1