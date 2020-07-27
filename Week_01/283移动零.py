"""
283. 移动零
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
通过次数180,152提交次数291,574


解题思路：
1.使用一个数组记录0的位置
非0数字都往前放，放到最靠前的0的位置

2.基于第一种方法，使用两个指针，1指针保存最近的0的位置，2指针查找非0
3.官方的最优解，非0元素往前放置
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastNotZereIndex = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[lastNotZereIndex], nums[i] = nums[i], nums[lastNotZereIndex]
                lastNotZereIndex += 1


if __name__ == "__main__":
    s = Solution()
    nums = [0, 1, 0, 3, 12]
    s.moveZeroes(nums)
    print(nums)
