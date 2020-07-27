"""
66. 加一
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。
通过次数179,753提交次数401,284


解题思路：
【9】 == 【1，0】？
1.模拟加法：数组最后元素加1，如何等于10，置零，前一位加一,如下代码遍历一遍实现
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = []
        # 当初始和进位时，表示需要加一
        carry = 1
        # 循环遍历每个数，有进位就加1，没有就加0
        for i in range(len(digits) - 1, -1, -1):
            add = digits[i] + carry
            if add == 10:
                ans.append(0)
                carry = 1
            else:
                ans.append(add)
                carry = 0
        if carry == 1:
            ans.append(1)
        ans.reverse()
        return ans


if __name__ == "__main__":
    s = Solution()
    assert s.plusOne([9]) == [1, 0]
    assert s.plusOne([2, 9]) == [3, 0]
    assert s.plusOne([3, 3, 3]) == [3, 3, 4]
