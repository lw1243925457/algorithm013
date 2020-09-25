# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。 
# 
#  机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。 
# 
#  现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？ 
# 
#  
# 
#  网格中的障碍物和空位置分别用 1 和 0 来表示。 
# 
#  说明：m 和 n 的值均不超过 100。 
# 
#  示例 1: 
# 
#  输入:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# 输出: 2
# 解释:
# 3x3 网格的正中间有一个障碍物。
# 从左上角到右下角一共有 2 条不同的路径：
# 1. 向右 -> 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右 -> 向右
#  
#  Related Topics 数组 动态规划 
#  👍 415 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    """
    解题思路：
    一、动态规划：情况同不同路径,只是多了一个障碍物的处理
    dp[i][j]:
        如果i,j为障碍物，则dp[i][j]为0
        如果不是，则dp[i][j] = dp[i-1][j] + dp[i][j-1]

    """
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
            return 0
        height, width = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[1] * width for _ in range(0, height)]
        for i in range(0, height):
            for j in range(0, width):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    dp[i][j] = dp[i][j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
# leetcode submit region end(Prohibit modification and deletion)
