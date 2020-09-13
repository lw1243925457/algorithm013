# 编写一个程序，通过已填充的空格来解决数独问题。 
# 
#  一个数独的解法需遵循如下规则： 
# 
#  
#  数字 1-9 在每一行只能出现一次。 
#  数字 1-9 在每一列只能出现一次。 
#  数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。 
#  
# 
#  空白格用 '.' 表示。 
# 
#  
# 
#  一个数独。 
# 
#  
# 
#  答案被标成红色。 
# 
#  Note: 
# 
#  
#  给定的数独序列只包含数字 1-9 和字符 '.' 。 
#  你可以假设给定的数独只有唯一解。 
#  给定数独永远是 9x9 形式的。 
#  
#  Related Topics 哈希表 回溯算法 
#  👍 526 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    """
    解题思路：
    一、暴力枚举求解：注意行列，3X3方格的处理，因为数据大小固定为9X9，则时间复杂度为O(1)
    """
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [[0] * 10 for _ in range(0, 9)]
        cols = [[0] * 10 for _ in range(0, 9)]
        boxs = [[0] * 10 for _ in range(0, 9)]

        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] != ".":
                    num = int(board[i][j])
                    rows[i][num] = 1
                    cols[j][num] = 1
                    boxs[(i // 3) * 3 + j // 3][num] = 1

        self._fill(board, 0, 0, rows, cols, boxs)

    def _fill(self, board, row, col, rows, cols, boxs):
        if not 0 <= row < 9 or not 0 <= col < 9:
            return True

        nextRow, nextCol = row, col + 1
        if nextCol >= 9:
            nextRow += 1
            nextCol = 0

        num = board[row][col]
        if num != ".":
            return self._fill(board, nextRow, nextCol, rows, cols, boxs)
        else:
            for i in range(1, 10):
                if rows[row][i] == 1 or cols[col][i] == 1 or boxs[(row // 3) * 3 + col // 3][i] == 1:
                    continue
                rows[row][int(i)] = 1
                cols[col][int(i)] = 1
                boxs[(row // 3) * 3 + col // 3][int(i)] = 1
                board[row][col] = str(i)
                if self._fill(board, nextRow, nextCol, rows, cols, boxs):
                    return True
                else:
                    board[row][col] = "."
                rows[row][int(i)] = 0
                cols[col][int(i)] = 0
                boxs[(row // 3) * 3 + col // 3][int(i)] = 0
        return False


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    Solution().solveSudoku(board)
    for item in board:
        print(item)

