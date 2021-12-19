from typing import List
import collections
class TreeNode:
    def __init__(self, left=None, right=None, val=0) -> None:
        self.val = val 
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = []
        res = collections.deque()
        
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                res.appendleft(cur.val)
                cur = cur.right 
            else:
                node = stack.pop()
                cur = node.left
        return res


ins = Solution()

