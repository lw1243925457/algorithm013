# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。 
# 
#  
# 
#  示例： 
# 
#  输入：n = 3
# 输出：[
#        "((()))",
#        "(()())",
#        "(())()",
#        "()(())",
#        "()()()"
#      ]
#  
#  Related Topics 字符串 回溯算法 
#  👍 1299 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    """
    解题思路：
    一、递归回溯：
    1.当前位置有两种选择，生成左括号或者生成右括号
    2.剪枝：当处于第一个位置、前面左右括号相等时，只能生成左括号
    每次有两个选择，递归树类似二叉树，则时间复杂度大致为O(2^N)
    """
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self._create(n, n, [], ans)
        return ans

    def _create(self, left, right, path, ans):
        if left == 0 and right == 0:
            ans.append("".join(path))
            return
        if left > 0:
            path.append("(")
            self._create(left - 1, right, path, ans)
            path.pop()
        if right > left:
            path.append(")")
            self._create(left, right - 1, path, ans)
            path.pop()
# leetcode submit region end(Prohibit modification and deletion)
