

from typing import List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val 
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        que = deque()
        que.append(root)
        ans = 0

        while que:
            sz = len(que)
            while sz > 0:
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                sz -= 1
            ans += 1
        
        return ans