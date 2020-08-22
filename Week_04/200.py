"""
200. 岛屿数量
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。



示例 1:

输入:
[
['1','1','1','1','0'],
['1','1','0','1','0'],
['1','1','0','0','0'],
['0','0','0','0','0']
]
输出: 1
示例 2:

输入:
[
['1','1','0','0','0'],
['1','1','0','0','0'],
['0','0','1','0','0'],
['0','0','0','1','1']
]
输出: 3
解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。


解题思路：
遍历数据，遇到1时同相连的1置为0,统计累计数量
每个数据最多访问两次，则事件复杂度应该为O(N)
这种题关键是套路，和围棋类似那题很像
"""
from typing import List


class Solution:
    def __init__(self):
        self.grid = None
        self.n, self.m = 0, 0

    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        self.grid = grid
        self.n, self.m = len(grid), len(grid[0])
        ans = 0
        for i in range(0, self.n):
            for j in range(0, self.m):
                if self.grid[i][j] == "1":
                    ans += 1
                    self.merge(i, j)
        return ans

    def merge(self, x, y):
        if x < 0 or x >= self.n or y < 0 or y >= self.m or self.grid[x][y] != "1":
            return
        self.grid[x][y] = "0"
        self.merge(x + 1, y)
        self.merge(x - 1, y)
        self.merge(x, y + 1)
        self.merge(x, y - 1)


if __name__ == "__main__":
    solution = Solution()
    grid = [
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1']
    ]
    print(solution.numIslands(grid))
