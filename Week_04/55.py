"""
55. 跳跃游戏
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。

示例 1:

输入: [2,3,1,1,4]
输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
示例 2:

输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。


解题思路：
使用贪心，从后往前，尽量往前走，能走到0则可以跳跃
但更新查找靠前的一跳位置比较耗时，导致程序超时。。。。。。

动态规划和贪心类的问题不是太熟练，得多练练

https://leetcode-cn.com/problems/jump-game/solution/55-by-ikaruga/
上面的思路很巧妙：遍历生成最大能跳跃的位置即可，有点像动态规划，又好像不是
需要注意的是每步都有判断前面最大跳跃是否能跳到这
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return True

        maxStep = 0
        for i in range(0, n):
            if maxStep < i:
                return False
            maxStep = max(maxStep, i+nums[i])
        return True


if __name__ == "__main__":
    solution = Solution()
    assert solution.canJump([2, 3, 1, 1, 4])
    assert not solution.canJump([3, 2, 1, 0, 4])
