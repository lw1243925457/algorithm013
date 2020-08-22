"""
33. 搜索旋转排序数组
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1
通过次数151,798提交次数395,337

解题思路：
看了官方的二分思路，真想不到这样也能二分
1.照常寻找mid
2.判断左或右部分是否有序（可能会存在三种情况，左右其中一个有序，或者两个都有序，但都不影响，左不有序，右有序）
3.target与有序部分比较，确定下面的搜索范围或者相等直接返回

二分还是写的不熟练啊，使用递归和不递归差别大吗？后面还得练练啊
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        return self.binarySearch(nums, target, 0, len(nums)-1)

    def binarySearch(self, nums: List[int], target: int, left: int, right: int) -> int:
        print(left, right, int((left + right) / 2), nums)
        if left == right and nums[left] != target:
            return -1

        mid = int((left + right) / 2)
        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            if nums[mid] >= target >= nums[left]:
                return self.binarySearch(nums, target, left, mid)
            else:
                return self.binarySearch(nums, target, mid+1, right)
        else:
            if nums[right] >= target >= nums[mid]:
                return self.binarySearch(nums, target, mid+1, right)
            else:
                return self.binarySearch(nums, target, left, mid)


if __name__ == "__main__":
    s = Solution()
    print(s.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))
    print(s.search(nums=[4, 5, 6, 7, 0, 1, 2, 3], target=0))
    print(s.search(nums=[4, 5, 6, 7, 0, 1, 2], target=3))
    print(s.search(nums=[1], target=1))
    print(s.search(nums=[5, 1, 3], target=5))
