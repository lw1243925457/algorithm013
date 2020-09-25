# 给定一个无序的整数数组，找到其中最长上升子序列的长度。 
# 
#  示例: 
# 
#  输入: [10,9,2,5,3,7,101,18]
# 输出: 4 
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。 
# 
#  说明: 
# 
#  
#  可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。 
#  你算法的时间复杂度应该为 O(n2) 。 
#  
# 
#  进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗? 
#  Related Topics 二分查找 动态规划 
#  👍 1008 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    """
    解题思路：
    一、暴力法：遍历统计当前数由多少个小于它的数字，初始都为1
    1.第一层遍历所有数
    3.第二层遍历第一层当前数左边数字，选择小于其数且长度最长的值，加上当前数即可
    两层遍历，时间复杂度O(N^2)
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        size = len(nums)
        dp = [1] * size
        for i in range(0, size):
            leastNum = None
            for j in range(0, i):
                if nums[j] < nums[i]:
                    if leastNum is None:
                        leastNum = j
                    elif dp[leastNum] < dp[j]:
                        leastNum = j
            # print(leastNum)
            if leastNum is not None:
                dp[i] = dp[i] + dp[leastNum]
        # print(dp)
        return max(dp)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    assert Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert Solution().lengthOfLIS([]) == 0
    assert Solution().lengthOfLIS([1]) == 1
