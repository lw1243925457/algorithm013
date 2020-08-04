"""
剑指 Offer 49. 丑数
我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。



示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:

1 是丑数。
n 不超过1690。
注意：本题与主站 264 题相同：https://leetcode-cn.com/problems/ugly-number-ii/


解题思路：
1刷

自己的思路都不对，直接文抄公大佬的答案
思想是用三指针保存2， 3， 5当前得到最大数的位置，下一个数就从这三个数乘得到，注意一点是重复值解决是值相同时指针都向后移
"""


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 0:
            return 0

        ans = [1] * n
        p2, p3, p5 = 0, 0, 0

        for i in range(1, n):
            v2 = ans[p2] * 2
            v3 = ans[p3] * 3
            v5 = ans[p5] * 5
            ans[i] = min(min(v2, v3), v5)

            if ans[i] == v2:
                p2 += 1
            if ans[i] == v3:
                p3 += 1
            if ans[i] == v5:
                p5 += 1

        return ans[-1]


if __name__ == "__main__":
    s = Solution()
    print(s.nthUglyNumber(10))
