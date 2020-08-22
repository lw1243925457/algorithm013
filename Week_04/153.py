"""
153. 寻找旋转排序数组中的最小值
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

你可以假设数组中不存在重复元素。

示例 1:

输入: [3,4,5,1,2]
输出: 1
示例 2:

输入: [4,5,6,7,0,1,2]
输出: 0


解题思路：
解法1：
参考官方题解，这种题感觉有点像找规律。。。。。。
变化点左侧元素大于第一个元素
变化点右侧元素小于第一个元素

当mid > mid + 1 or mid-1 < mid时就是变化点，返回即可
当mid > left 时，左边有序的，搜索右边，反之

解法2：
提交区的发现的一个思路：判断最左值是否小于最右值即可
感觉搜索次数应该比方法1多，比较方法1中间就可能找到答案，而它要到最后

两种方法时间复杂度都是O(logN)
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return nums[0]

        if nums[0] < nums[-1]:
            return nums[0]

        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[left] < nums[mid]:
                left = mid + 1
            else:
                right = mid - 1


if __name__ == "__main__":
    solution = Solution()
    assert solution.findMin([3, 4, 5, 1, 2]) == 1
