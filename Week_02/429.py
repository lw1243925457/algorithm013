"""
429. N叉树的层序遍历
给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。

例如，给定一个 3叉树 :







返回其层序遍历:

[
     [1],
     [3,2,4],
     [5,6]
]


说明:

树的深度不会超过 1000。
树的节点总数不会超过 5000。


解题思路：
1，非递归，两个数组，一个当前层的遍历，另一个保存用于获取下一次
"""
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        ans = []
        stackGet = [root]
        stackSave = []
        while stackGet:
            l = []
            while stackGet:
                node = stackGet.pop()
                l.append(node.val)
                stackSave.append(node)
            ans.append(l)

            while stackSave:
                node = stackSave.pop()
                for i in range(len(node.children)-1 , -1, -1):
                    stackGet.append(node.children[i])

        return ans
