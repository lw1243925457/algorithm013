"""
45. 跳跃游戏 II
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
说明:

假设你总是可以到达数组的最后一个位置。


解题思路：
方法1：
使用动态规划
当前位置所需最小步数=min（nums【：i】）+1
遍历生成dp一次，内嵌最小步数查找一次，时间复杂度O(N^2),超时

方法2：
参考官方题解
从头遍历数组，记录下能跳最远距离的下标，当下标更新时步数加1
就是跳跃游戏I，加了个步数判断
注意的点是，步数加一的条件判断
数据遍历一次，时间复杂度O(N)
"""
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        steps = 0
        end = 0
        maxPos = 0
        for i in range(0, n - 1):
            maxPos = max(maxPos, i + nums[i])
            if i == end:
                end = maxPos
                steps += 1
        return steps


if __name__ == "__main__":
    solution = Solution()
    print(solution.jump([2, 3, 1, 1, 4]))
    print(solution.jump([3, 2, 1]))
