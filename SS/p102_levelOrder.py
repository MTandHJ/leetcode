from typing import List


class TreeNode:
    def __init__(self, val, left, right) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            res.append([node.val for node in queue])
            oldQueue = queue
            queue = []
            for node in oldQueue:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return res

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 单位情况
        if not root: return []
        # 最后的结果
        res = []
        # 当前层的结点
        queue = [root]
        # 每一层取val的值
        while queue:
            # 当前层结点val值的存放列表
            tmp = []
            for _ in range(len(queue)):
                # 出队列
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # 添加上当前层的结点值
            res.append(tmp)
        return res

# 对比两者：
# 1、 前者有两个for循环
# 2、后者只有一个for循环，在循环的过程也处理了queue中的元素。
# 相当于是变添加边删除（就相当于是第一次的queue的for循环，以及最后的pop操作

