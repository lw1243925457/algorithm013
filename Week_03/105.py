"""
105. 从前序与中序遍历序列构造二叉树
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
通过次数102,596提交次数151,616


解题思路：
暂用方法一

1.根据前序后中序遍历特地，还原二叉树
    1.根据前序找到当前的父亲节点（既第一个元素）
    2.在中序中，父亲节点两侧便是左子树和右子树，找到左右子树范围
    3.递归还原左右子树

2.1方法改进：
    1方法中中序父亲节点位置的查找优化，使用字典存储好
    2.1方法中的空间优化，使用位置参数代替数组参数

数据都只访问了一次，时间复杂度是O(N)
第一种方法中每次新建一个数组空间，N(N+1)/2的大小，加上递归栈，空间复杂度大致为O(N)
第二种方法没有新建数组之类的，空间复杂度为O(1)
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 第二种方法
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None

        index = {element: i for i, element in enumerate(inorder)}

        def create(preLeft, preRight, inLeft, inRight) -> TreeNode:
            """
            preLeft为当前树的父节点
            在中序中查找preLeft的值，确定左右子树的左右边界
            :param preLeft:
            :param preRight:
            :param inLeft:
            :param inRight:
            :return:
            """
            if preLeft > preRight:
                return None

            # 构造根节点
            root = TreeNode(preorder[preLeft])
            # 获取中序中根节点的位置，求出左子树节点数目
            rootIndex = index[preorder[preLeft]]
            leftAmount = rootIndex-inLeft
            # 构造左右子树
            root.left = create(preLeft+1, preLeft+leftAmount, inLeft, rootIndex-1)
            root.right = create(preLeft+1+leftAmount, preRight, rootIndex+1, inRight)
            return root

        n = len(preorder)
        return create(0, n-1, 0, n-1)


"""
# 第一种方法
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None

        def build(preorder: List[int], inorder: List[int]) -> TreeNode:
            if len(preorder) == 0:
                return None
            if len(preorder) == 1:
                return TreeNode(preorder[0])

            root = TreeNode(preorder[0])
            splitIndex = inorder.index(preorder[0])
            root.left = build(preorder[1:splitIndex + 1], inorder[:splitIndex])
            root.right = build(preorder[splitIndex + 1:], inorder[splitIndex + 1:])
            return root

        return build(preorder, inorder)
"""


def dfs(node: TreeNode):
    if node:
        print(node.val, end=" ")
        dfs(node.left)
        dfs(node.right)
    else:
        print("null", end=" ")


if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    solution = Solution()
    dfs(solution.buildTree(preorder, inorder))
    print()

    preorder = [1, 2]
    inorder = [2, 1]
    solution = Solution()
    dfs(solution.buildTree(preorder, inorder))
    print()
