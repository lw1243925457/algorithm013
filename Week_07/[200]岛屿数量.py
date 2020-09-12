# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。 
# 
#  岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。 
# 
#  此外，你可以假设该网格的四条边均被水包围。 
# 
#  
# 
#  示例 1: 
# 
#  输入:
# [
# ['1','1','1','1','0'],
# ['1','1','0','1','0'],
# ['1','1','0','0','0'],
# ['0','0','0','0','0']
# ]
# 输出: 1
#  
# 
#  示例 2: 
# 
#  输入:
# [
# ['1','1','0','0','0'],
# ['1','1','0','0','0'],
# ['0','0','1','0','0'],
# ['0','0','0','1','1']
# ]
# 输出: 3
# 解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 
#  👍 761 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    """
    解题思路：
    一、深度优先搜索：遇到为1，岛屿加一，将其相邻岛屿及其置零
    时间复杂度为O(N^2)

    二、并查集
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        height, width = len(grid), len(grid[0])
        ans = 0
        for i in range(0, height):
            for j in range(0, width):
                if grid[i][j] == "1":
                    ans += 1
                    self._remove(grid, i, j, height, width)
        return ans

    def _remove(self, grid, i, j, height, width):
        if not 0 <= i < height or not 0 <= j < width or grid[i][j] == "0":
            return
        grid[i][j] = "0"
        self._remove(grid, i - 1, j, height, width)
        self._remove(grid, i + 1, j, height, width)
        self._remove(grid, i, j - 1, height, width)
        self._remove(grid, i, j + 1, height, width)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    assert Solution().numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]) == 1