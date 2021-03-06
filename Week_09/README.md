# 学习笔记(第九周)
***
## 不同路径II 解题
```python
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
```