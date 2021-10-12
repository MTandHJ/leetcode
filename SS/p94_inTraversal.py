
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val 
        self.left = left
        self.right = right
    
class Solution:
    def inTraversal(self, root: TreeNode) -> List[int]:
        WHITE, GRAY = 0, 1
        stack = [(WHITE, root)]
        res = []
        while stack:
            color, node = stack.pop()
            if not node: continue
            if color == WHITE:
                stack.append((WHITE, root.left))
                stack.append((GRAY, node))
                stack.append((WHITE, root.right))
            else:
                res.append(node.val)
        
        return res

class Solution:
    def inTraversal(self, root: TreeNode) -> List[int]:
        res = []
        cur = root
        stack = [root]
        while cur and stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right

        return res
    
    def inTraversal2(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            if root.right:
                stack.append(root.right)
        return res