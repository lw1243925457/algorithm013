"""
144. 二叉树的前序遍历
给定一个二叉树，返回它的 前序 遍历。

 示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,2,3]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？


解题思路：
前序遍历：中左右
递归还是很好理解
非递归，这个入栈顺序需要注意：弹出当前中，如右，如左（因为是后进先出，则会先放我左）
"""
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        ans = []

        def preorder(root: TreeNode):
            """递归实现"""
            ans.append(root.val)
            if root.left:
                preorder(root.left)
            if root.right:
                preorder(root.right)

        def preorder2(root: TreeNode):
            """非递归实现"""
            cur = root
            stack = [cur]
            while stack:
                node = stack.pop()
                ans.append(node.val)

                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)

        # preorder(root)
        preorder2(root)
        return ans
