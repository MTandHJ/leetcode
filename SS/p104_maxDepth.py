
import collections

class TreeNode:
    def __init__(self, left=None, right=None, val=0) -> None:
        self.left = left
        self.right = right
        self.val = val
class Solution:
    # BFS
    def maxDepth(root: TreeNode) -> int:
        if not root:
            return 0
        que = collections.deque()
        que.append(root)
        res = 0
        while que:
            sz = len(que)
            while sz > 0:
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                sz -= 1
            res += 1
        
        return res
