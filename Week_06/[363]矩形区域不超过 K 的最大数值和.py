# 给定一个非空二维矩阵 matrix 和一个整数 k，找到这个矩阵内部不大于 k 的最大矩形和。 
# 
#  示例: 
# 
#  输入: matrix = [[1,0,1],[0,-2,3]], k = 2
# 输出: 2 
# 解释: 矩形区域 [[0, 1], [-2, 3]] 的数值和是 2，且 2 是不超过 k 的最大数字（k = 2）。
#  
# 
#  说明： 
# 
#  
#  矩阵内的矩形区域面积必须大于 0。 
#  如果行数远大于列数，你将如何解答呢？ 
#  
#  Related Topics 队列 二分查找 动态规划 
#  👍 119 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import bisect
from typing import List


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        row, col = len(matrix), len(matrix[0])
        res = float('-inf')
        # 左边界
        for left in range(col):
            # 初始化nums（这个nums就是我们后面要用来求接近K的）
            nums = [0] * row
            # 右边界
            for right in range(left, col):
                for i in range(row):
                    nums[i] += matrix[i][right]
                # 在left, right为边界下的矩阵(在这里已经降维成1维的nums了)，
                # 下面这段求不超过k的最大数值和（跟前面我们讲的如出一辙）
                # 用来存cum的array（已排序）
                array = [0]
                cum = 0
                for num in nums:
                    cum += num
                    loc = bisect.bisect_left(array, cum - k)
                    if loc < len(array):
                        res = max(res, cum - array[loc])
                    bisect.insort(array, cum)
        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    Solution().maxSumSubmatrix(matrix = [[1,0,1],[0,-2,3]], k = 2)
