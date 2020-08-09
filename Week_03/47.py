"""
47. 全排列 II
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]


解题思路：
一个解题规律：看到不重复问题的排列组合类的，可以使用排序+此次选取中不等于上次值来达到目的
"""
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 2:
            return [nums]

        ans = []

        def create(array: List[int], l: List[int]):
            if len(array) == 0:
                ans.append(l.copy())
                return

            for i in range(0, len(array)):
                if i > 0 and array[i] == array[i-1]:
                    continue
                l.append(array[i])
                create(array[:i] + array[i + 1:], l)
                l.pop()

        nums = sorted(nums)
        create(nums, [])
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.permuteUnique([1, 2, 1]))
