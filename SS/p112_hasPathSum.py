import collections
from typing import Collection, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum
        
        return self.hasPathSum(root.left, targetSum-root.val) \
            or self.hasPathSum(root.right, targetSum-root.val)
        
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        
        que_node = collections.deque()
        que_val = collections.deque()

        while que_node:
            node = que_node.popleft()
            val = que_val.popleft()
            if not node.left and not node.right:
                if val == targetSum:
                    return True
                continue
            # 注意下面一定要加上一个当前层的val
            if node.left:
                que_node.append(node.left)
                que_val.append(node.left.val + val)
            if node.right:
                que_node.append(node.right)
                que_val.append(node.right.val + val)
        return False