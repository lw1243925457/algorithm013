# 给出一个区间的集合，请合并所有重叠的区间。 
# 
#  
# 
#  示例 1: 
# 
#  输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#  
# 
#  示例 2: 
# 
#  输入: intervals = [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。 
# 
#  注意：输入类型已于2019年4月15日更改。 请重置默认代码定义以获取新方法签名。 
# 
#  
# 
#  提示： 
# 
#  
#  intervals[i][0] <= intervals[i][1] 
#  
#  Related Topics 排序 数组 
#  👍 602 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    """
    解题思路：
    一、参考官方题解，证明有点复杂，大致意思就是，上一个元素右值小于下一个元素左值则两者不能合并，反之进行合并
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        # print(intervals)
        ans = []
        for item in intervals:
            if not ans or ans[-1][1] < item[0]:
                ans.append(item)
            else:
                ans[-1][1] = max(ans[-1][1], item[1])
        return ans


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    Solution().merge([[2, 6], [8, 10], [1, 3], [15, 18]])
