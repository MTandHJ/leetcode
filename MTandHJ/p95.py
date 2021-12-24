

from typing import Collection, List

from base import version


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTrees(self, low:int, high: int):
        if low == high:
            return [TreeNode(low)]
        if low > high:
            return [None]
        trees = []
        for node in range(low, high + 1):
            left = self.buildTrees(low, node - 1)
            right = self.buildTrees(node + 1, high)
            for lchild in left:
                for rchild in right:
                    trees.append(
                        TreeNode(node, lchild, rchild)
                    )
        return trees


    @version("36ms, 16.7mb")
    def generateTrees(self, n: int) -> List[TreeNode]:
        return self.buildTrees(1, n)
