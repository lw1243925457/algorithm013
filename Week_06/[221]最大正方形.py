# 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。 
# 
#  示例: 
# 
#  输入: 
# 
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# 
# 输出: 4 
#  Related Topics 动态规划 
#  👍 534 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    """
    解题思路：
    一：动态规划
    1.重复子结构：当前格子能组成的正方形取决于去左，左上，上
    2.递归状态：dp[i][j]
    3.递推公式：dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
    按道理讲，也就遍历了一次，O(NM)的复杂度吧，咋感觉很慢呢
    """
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ans = 0
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if i == 0 or j == 0:
                    ans = max(int(matrix[i][j]), ans)
                    continue
                if int(matrix[i][j]) == 0 or int(matrix[i-1][j]) == 0 or int(matrix[i][j-1]) == 0 or int(matrix[i-1][j-1]) == 0:
                    ans = max(int(matrix[i][j]), ans)
                    continue
                matrix[i][j] = min(int(matrix[i-1][j]), int(matrix[i-1][j-1]), int(matrix[i][j-1])) + 1
                ans = max(matrix[i][j], ans)
        return ans**2
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    matrix = [[1,0,1,0,0], [1,0,1,1,1],[1,1,1,1,1],[1,0,0,1,0]]
    print(Solution().maximalSquare(matrix))
    print(Solution().maximalSquare([["1"]]))
    print(Solution().maximalSquare([["0"]]))
    print(Solution().maximalSquare([["0", "1"]]))
    matrix = [["0","0","0","0","0"],["0","0","0","0","0"],["0","0","0","0","1"],["0","0","0","0","0"]]
    print(Solution().maximalSquare(matrix))
    for i in matrix:
        print(i)
