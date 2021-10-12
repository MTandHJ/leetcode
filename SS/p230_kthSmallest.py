

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self._cnt = 0
        self._val = 0
        def inorder(root: TreeNode, k: int):
            if not root:
                return 
            inorder(root.left, k)
            self._cnt += 1
            if self._cnt == k:
                val = root.val
                return 
            inorder(root.right, k)
        
        inorder(root, k)
        return self.val

