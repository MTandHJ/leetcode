import collections
from typing import TextIO


class TreeNode:
    def __init__(self, left=None, right=None, val=0):
        self.left = left
        self.right = right
        self.val = val

class Solution:
    def minDepth(self, root: TreeNode):
        if not root:
            return 0
        self.res = float('inf')
        
        return self.res
    
    def depth(self, root: TreeNode) -> int:
        # if not root:
        #     return 0
        # cur_depth = 1 + min(self.depth(root.left), self.depth(root.right))
        # self.res = min(self.res, cur_depth)
        # return 1 + cur_depth
        # if not root:
        #     return 0

        # left = self.minDepth(root.left)
        # right = self.minDepth(root.right)
        # if left == 0 or right == 0:
        #     return left + right + 1
        # return min(left, right) + 1



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # BFS 找最短路径
    # DFS是线， BFS是面
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        # 建立队列
        que = collections.deque()
        que.append(root)
        depth = 1

        while que:
            # 这代表树中的一行
            sz = len(que)
            # 遍历一行中的每个节点
            for i in range(sz):
                cur = que.popleft()
                # 到达叶子节点
                if not cur.left and not cur.right:
                    return depth
                # 建立下一行，为遍历下一行做准备
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            # 一个for循环结束，代表一行遍历结束
            depth += 1
        return depth