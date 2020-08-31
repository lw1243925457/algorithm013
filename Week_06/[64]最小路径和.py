# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。 
# 
#  说明：每次只能向下或者向右移动一步。 
# 
#  示例: 
# 
#  输入:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。
#  
#  Related Topics 数组 动态规划 
#  👍 649 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    """
    解题思路：
    一：暴力递归求解：从0.0开始，递归出所有路径的和，返回小的
    每个格子有两个选择，则为递归树，时间复杂度为O(2^N)

    二：动态规划：当前格子的最小和为能移动到它的格子中的最小值加上本身
    1.最优子结构 当前格子 = min（上格子，左格子） + 当前格子
    2.存储中间状态 dp[i][j]
    3.递推公式 dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + dp[i][j]
    对第一行和第一列进行特殊处理，每个数据访问一次，时间复杂度为O(N)
    """
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        rows, cols = len(grid), len(grid[0])
        for i in range(0, rows):
            for j in range(0, cols):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    grid[i][j] = grid[i][j-1] + grid[i][j]
                    continue
                if j == 0:
                    grid[i][j] = grid[i-1][j] + grid[i][j]
                    continue
                grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
        return grid[-1][-1]
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    grid = [[1, 3, 1],[1, 5, 1],[4, 2, 1]]
    assert Solution().minPathSum(grid) == 7
