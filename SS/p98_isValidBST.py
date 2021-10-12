

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def bst(root: TreeNode, lower:int, upper: int) -> bool:
            if not root:
                return True
            if root.val >= upper or root.val <= lower:
                return False
            
            return bst(root.left, lower, root.val) & bst(root, root.val, upper)
        
        return bst(root, -float('INF'), float('INF'))