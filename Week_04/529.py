"""
529. 扫雷游戏
让我们一起来玩扫雷游戏！

给定一个代表游戏板的二维字符矩阵。 'M' 代表一个未挖出的地雷，'E' 代表一个未挖出的空方块，'B' 代表没有相邻（上，下，左，右，和所有4个对角线）地雷的已挖出的空白方块，数字（'1' 到 '8'）表示有多少地雷与这块已挖出的方块相邻，'X' 则表示一个已挖出的地雷。

现在给出在所有未挖出的方块中（'M'或者'E'）的下一个点击位置（行和列索引），根据以下规则，返回相应位置被点击后对应的面板：

如果一个地雷（'M'）被挖出，游戏就结束了- 把它改为 'X'。
如果一个没有相邻地雷的空方块（'E'）被挖出，修改它为（'B'），并且所有和其相邻的未挖出方块都应该被递归地揭露。
如果一个至少与一个地雷相邻的空方块（'E'）被挖出，修改它为数字（'1'到'8'），表示相邻地雷的数量。
如果在此次点击中，若无更多方块可被揭露，则返回面板。


示例 1：

输入:

[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]

输出:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

解释:

示例 2：

输入:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Click : [1,2]

输出:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'X', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

解释:



注意：

输入矩阵的宽和高的范围为 [1,50]。
点击的位置只能是未被挖出的方块 ('M' 或者 'E')，这也意味着面板至少包含一个可点击的方块。
输入面板不会是游戏结束的状态（即有地雷已被挖出）。
简单起见，未提及的规则在这个问题中可被忽略。例如，当游戏结束时你不需要挖出所有地雷，考虑所有你可能赢得游戏或标记方块的情况。


解题思路：
模拟即可，注意不是地雷方块的递归揭露和相邻地雷计算
"""
from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def dfs(x, y):
            # 不为E则代表访问过了
            if board[x][y] != "E":
                return
            # 设置为中间态，代表访问过了
            board[x][y] = "S"
            mines = 0
            nextPos = []
            # 遍历当前位置的周围8个方向，记录地雷格式和相邻坐标
            for dir in dirs:
                nextx, nexty = x + dir[0], y + dir[1]
                if nextx < 0 or nextx >= n or nexty < 0 or nexty >= m:
                    continue
                if board[nextx][nexty] == "M":
                    mines += 1
                    continue
                nextPos.append([nextx, nexty])
            # 如果没有地雷，递归相邻坐标
            if mines == 0:
                board[x][y] = "B"
                for pos in nextPos:
                    dfs(pos[0], pos[1])
            else:
                board[x][y] = str(mines)

        # 点到雷直接赋值返回
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board

        n, m = len(board), len(board[0])
        dirs = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        dfs(click[0], click[1])
        return board


if __name__ == "__main__":
    solution = Solution()

    board = [['E', 'E', 'E', 'E', 'E'],
             ['E', 'E', 'M', 'E', 'E'],
             ['E', 'E', 'E', 'E', 'E'],
             ['E', 'E', 'E', 'E', 'E']]
    click = [3, 0]
    solution.updateBoard(board, click)
    for item in board:
        print(item)
    print("*********************************")

    board = [['E', 'E', 'M', 'E', 'E'],
             ['E', 'E', 'M', 'E', 'E'],
             ['E', 'E', 'M', 'E', 'E'],
             ['E', 'E', 'M', 'E', 'E']]
    click = [3, 0]
    solution.updateBoard(board, click)
    for item in board:
        print(item)
    print("*********************************")

    board = [['E', 'E', 'M', 'E', 'E'],
             ['E', 'E', 'M', 'E', 'E'],
             ['E', 'E', 'M', 'E', 'E'],
             ['E', 'E', 'M', 'E', 'E']]
    click = [3, 2]
    solution.updateBoard(board, click)
    for item in board:
        print(item)
