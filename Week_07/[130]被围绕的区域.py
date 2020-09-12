# 给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。 
# 
#  找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。 
# 
#  示例: 
# 
#  X X X X
# X O O X
# X X O X
# X O X X
#  
# 
#  运行你的函数后，矩阵变为： 
# 
#  X X X X
# X X X X
# X X X X
# X O X X
#  
# 
#  解释: 
# 
#  被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被
# 填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。 
#  Related Topics 深度优先搜索 广度优先搜索 并查集 
#  👍 363 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    """
    解题思路：
    一、深度优先搜索：首先在边上的O是不会被围绕的，则与边上O相连的O也不会被围绕，有点类似围棋。。。。。。
    1.遍历四个边，将其及其相连的O置为S
    2.遍历整个数据，将非S置为X
    3.遍历整个数据，将S值为O
    每个数据遍历了最大三次，则时间复杂度为O(MN)
    """
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0 or len(board[0]) == 0:
            return
        height, width = len(board), len(board[0])

        # 处理第一列和最后一列，O置为S
        for i in range(0, height):
            self._modify(board, i, 0, height, width)
            self._modify(board, i, width - 1, height, width)
        # 处理第一行和最后一行，O置为S
        for i in range(0, width):
            self._modify(board, 0, i, height, width)
            self._modify(board, height - 1, i, height, width)

        for i in range(0, height):
            for j in range(0, width):
                if board[i][j] == "S":
                    continue
                board[i][j] = "X"

        for i in range(0, height):
            for j in range(0, width):
                if board[i][j] == "S":
                    board[i][j] = "O"

    def _modify(self, board, row, col, height, width):
        if not 0 <= row < height or not 0 <= col < width or board[row][col] == "X" or board[row][col] == "S":
            return
        board[row][col] = "S"
        self._modify(board, row + 1, col, height, width)
        self._modify(board, row - 1, col, height, width)
        self._modify(board, row, col + 1, height, width)
        self._modify(board, row, col - 1, height, width)

# leetcode submit region end(Prohibit modification and deletion)
