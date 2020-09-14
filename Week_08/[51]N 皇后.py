# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。 
# 
#  
# 
#  上图为 8 皇后问题的一种解法。 
# 
#  给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。 
# 
#  每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。 
# 
#  
# 
#  示例： 
# 
#  输入：4
# 输出：[
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],
# 
#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# 解释: 4 皇后问题存在两个不同的解法。
#  
# 
#  
# 
#  提示： 
# 
#  
#  皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。 
#  
#  Related Topics 回溯算法 
#  👍 603 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    """
    解题思路：
    一、暴力破解：枚举每一行的各个位置，判断是否合理即可；这里需要注意的是左右斜行的处理
    左右斜行的转换处理很精妙
    时间复杂度最大为O(N^N)，但进行了剪枝

    二、使用位运算优化空间，技巧很妙，滋滋滋
    """

    def solveNQueens(self, n: int) -> List[List[str]]:
        # cols = [0] * n
        # lrow, rrow = {}, {}
        cols, lrow, rrow = 0, 0, 0

        ans = []
        # self._fill(0, n, [], ans, cols, lrow, rrow)
        self._fillDigit(0, n, [], ans, cols, lrow, rrow)
        return ans

    def _fillDigit(self, index, n, path, ans, cols, lrow, rrow):
        """使用位运算优化空间"""
        if index >= n:
            ans.append([])
            for i in range(0, n):
                s = ["."] * n
                s[path[i]] = "Q"
                ans[-1].append("".join(s))
            return

        availablePositions = ((1 << n) - 1) & (~(cols | lrow | rrow))
        while availablePositions:
            position = availablePositions & (-availablePositions)
            availablePositions = availablePositions & (availablePositions - 1)
            column = bin(position - 1).count("1")
            path.append(column)
            self._fillDigit(index + 1, n, path, ans, cols | position, (lrow | position) << 1, (rrow | position) >> 1)
            path.pop()

    def _fill(self, index, n, path, ans, cols, lrow, rrow):
        if index >= n:
            ans.append([])
            for i in range(0, n):
                s = ["."] * n
                s[path[i]] = "Q"
                ans[-1].append("".join(s))
            return

        for i in range(0, n):
            if cols[i] == 1 or lrow.get(index - i, 0) == 1 or rrow.get(index + i) == 1:
                continue
            cols[i], lrow[index - i], rrow[index + i] = 1, 1, 1
            path.append(i)
            self._fill(index + 1, n, path, ans, cols, lrow, rrow)
            cols[i], lrow[index - i], rrow[index + i] = 0, 0, 0
            path.pop()


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    result = Solution().solveNQueens(4)
    for i in result:
        for j in i:
            print(j)
        print("**********")
