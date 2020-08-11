"""
46. 全排列
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]


解题思路：
一次选一个数字，返回所有组合
三层循环遍历，时间复杂度最差应该是O(N^3)
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 2:
            return [nums]

        ans = []

        def create(array: List[int], l: List[int]):
            if len(array) == 0:
                ans.append(l.copy())
                return

            for i in range(0, len(array)):
                l.append(array[i])
                create(array[:i] + array[i + 1:], l)
                l.pop()

        create(nums, [])
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.permute([1, 2, 3]))
