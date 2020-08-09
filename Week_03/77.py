"""
77. 组合
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]


解题思路：
这是一个排列组合问题，使用递归实现即可，kk之间的组合
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == 0 or k == 0:
            return []

        def create(current, l: List[int], level):
            if level == k:
                ans.append(l.copy())
                return

            for i in range(current, n+1):
                l.append(i)
                create(i+1, l, level+1)
                l.pop()

        ans = []
        create(1, [], 0)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.combine(4, 2))