"""
94. 二叉树的中序遍历
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

通过次数206,214提交次数285,076


解题思路：
中序遍历：左，根，右
非递归理解起来还是有点难度，不太容易
"""
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return self.inorder2(root)

        # 递归实现
        ans = []

        def inorder(root: TreeNode):
            """递归实现：访问顺序，左中右"""
            if root.left:
                inorder(root.left)
            ans.append(root.val)
            if root.right:
                inorder(root.right)

        inorder(root)
        return ans

    def inorder2(self, root: TreeNode):
        """
        非递归实现:其完全正确实现还是有点难度
        关键点是注意入栈和出栈的顺序
        """
        ans = []
        stack = []
        cur = root
        while cur or stack:
            # 先入栈当前节点，后面添加左节点，这里左节点全在栈尾
            while cur:
                stack.append(cur)
                cur = cur.left

            # 出栈，入栈顺序已经是中、左，最后如右
            node = stack.pop()
            ans.append(node.val)
            cur = node.right
        return ans
