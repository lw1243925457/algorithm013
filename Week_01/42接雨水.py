"""
42. 接雨水
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。



上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
通过次数126,831提交次数244,388


解题思路：
1 刷
看其他人题解的思路基本上是没有想到，对他们栈的方式也是太理解。。。。。。

借鉴使用栈计算柱状图最大矩形面积的思路
在官方题解的基础上加上自己的理解写的代码，对于官方代码如何处理最高3的后面那段没有看的明白

这里的解法是：
注：最高值优先左边的值，所有遍历左半区时不会遇到栈不为空的情况
注：当前柱子上的积水为：栈底柱子高度-当前柱子高度，栈底柱子根据算法为左边最高
1.求出最高矩形，把其划分为左右两个区
2.对左右两个区，套用官方的类似解法：小于栈底的入栈，大于栈底则表示可以计算积水面积了
3.有可能出现后面的值都小于等于栈底，则最后进行情况累计积水
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # 三个柱子才有可能积水
        if len(height) < 3:
            return 0

        # 查找最高柱子的位置
        hindex = 0
        for i in range(1, len(height)):
            if height[i] > height[hindex]:
                hindex = i

        ans = 0
        stack = []

        # 左半区进行积水累计计算
        for i in range(0, hindex + 1):
            if len(stack) != 0 and height[i] > stack[0]:
                for j in range(1, len(stack)):
                    ans += stack[0] - stack[j]
                stack.clear()
            stack.append(height[i])

        stack.clear()
        # 右半区进行积水累计计算
        for i in range(len(height) - 1, hindex - 1, -1):
            if len(stack) != 0 and height[i] > stack[0]:
                for j in range(1, len(stack)):
                    ans += stack[0] - stack[j]
                stack.clear()
            stack.append(height[i])

        # 对特殊情况进行积水累计计算
        if len(stack) > 2:
            for j in range(1, len(stack)):
                ans += stack[0] - stack[j]

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(s.trap([2, 0, 2]))
