"""
589. N叉树的前序遍历
给定一个 N 叉树，返回其节点值的前序遍历。

例如，给定一个 3叉树 :







返回其前序遍历: [1,3,5,6,2,4]。



说明: 递归法很简单，你可以使用迭代法完成此题吗?

通过次数36,750提交次数49,765


解题思路
前序：根左右
使用递归即可
非递归使用模拟栈实现,学到了【】的extend方法，其中的逆序放入也是需要注意的点
"""
# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def __init__(self):
        self.ans = []

    def preorder(self, root: 'Node') -> List[int]:
        """递归实现"""
        if root:
            self.ans.append(root.val)
            for children in root.children:
                self.preorder(children)
        return self.ans

    def preoder2(self, root: 'Node')-> List[int]:
        """非递归实现"""
        if not root:
            return self.ans
        stack = [root]
        while stack:
            p = stack.pop()
            self.ans.append(p.val)
            stack.extend(p.children[::-1])
        return self.ans


