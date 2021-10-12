# Definition for a binary tree node.


import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root:
            return 0
        que = collections.deque()
        que.append(root)
        res = root.val
        while 1:
            # 最后que为空时，返回res的值
            if not que:
                return res
            # res是当前层的第一个节点的，元素值
            res = que[0].val
            sz = len(que)
            for _ in range(sz):
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            # res = que[0].val